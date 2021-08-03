def cached(func):
    _cache = {}

    def wrapped(*args):
        nonlocal _cache
        if args not in _cache:
            _cache[args] = func(*args)
        return _cache[args]
    return wrapped


@cached
def num_count_with_len(l):
    """Количество чисел длины l"""
    return 10**l - 10**(l - 1) if l > 0 else 0


@cached
def numbers_len_sum(l):
    """Сумма длин всех чисел с длинами от 1 до l включительно"""
    if l < 0:
        return 0
    return numbers_len_sum(l - 1) + l * num_count_with_len(l)


def block_len(block_num):
    """Длина блока (т. е. строки '1234567891011...str(block_num)'"""
    l = len(str(block_num))
    return numbers_len_sum(l - 1) + (block_num - 10 ** (l - 1) + 1) * l


def arith_sum(n):
    """Сумма всех чисел от 1 до n включительно"""
    return n * (n + 1) // 2


@cached
def block_len_sum_(l):
    """Суммарная длина всех блоков с длиной не превосходящей l"""
    if l <= 0:
        return 0
    num_count = num_count_with_len(l)
    len_sum = numbers_len_sum(l - 1)
    return block_len_sum_(l - 1) + len_sum * num_count + arith_sum(num_count) * l


def block_len_sum(block_num):
    """Суммарная длина всех блоков подряд вплоть до блока block_num включительно"""
    l = len(str(block_num))
    len_sum = numbers_len_sum(l - 1)
    num_count = block_num - (10 ** (l - 1)) + 1
    return block_len_sum_(l - 1) + len_sum * num_count + l * arith_sum(num_count)


def binary_search(call, val):
    start = 0
    end = 1
    while call(end) <= val:
        end *= 2
    result = start
    while start <= end:
        mid = (start + end) // 2
        if call(mid) <= val:
            start = mid + 1
            result = start
        else:
            end = mid - 1
    return result


cases = int(input())
for _ in range(cases):
    index = int(input()) - 1
    block_num = binary_search(block_len_sum, index)
    rel_index = index - block_len_sum(block_num - 1)
    number = binary_search(block_len, rel_index)
    digit = rel_index - block_len(number - 1)
    print(str(number)[digit])
