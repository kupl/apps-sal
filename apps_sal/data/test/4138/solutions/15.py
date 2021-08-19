def cached(func):
    _cache = {}

    def wrapped(*args):
        nonlocal _cache
        if args not in _cache:
            _cache[args] = func(*args)
        return _cache[args]
    return wrapped


def len_num(l):
    """Количество чисел длины l"""
    return 10 ** l - 10 ** (l - 1) if l > 0 else 0


@cached
def len_sum(l):
    """Сумма длин всех чисел, длина которых строго меньше чем l"""
    if l <= 1:
        return 0
    return len_sum(l - 1) + len_num(l - 1) * (l - 1)


def block_len(block_num):
    """Длина блока (т. е. строки '1234567891011...str(block_num)'"""
    l = len(str(block_num))
    return len_sum(l) + (block_num - 10 ** (l - 1) + 1) * l


def arith_sum(n):
    return n * (n + 1) // 2


@cached
def block_len_sum_(l):
    """Суммарная длина всех блоков длины меньшей чем l"""
    if l <= 0:
        return 0
    ln = len_num(l - 1)
    ls = len_sum(l - 1)
    return block_len_sum_(l - 1) + ls * ln + arith_sum(ln) * (l - 1)


def block_len_sum(block_num):
    """Суммарная длина всех блоков подряд вплоть до блока block_num
    Если l = len(str(block_num))
    """
    l = len(str(block_num))
    ls = len_sum(l)
    ln = block_num - 10 ** (l - 1) + 1
    return block_len_sum_(l) + ls * ln + l * arith_sum(ln)


def binary_search(call, val):
    start = 1
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
