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
    return 10**l - 10**(l - 1) if l > 0 else 0


@cached
def len_sum(l):
    """Сумма длин всех чисел, длина которых строго меньше чем l"""
    return len_sum(l - 1) + (len_num(l - 1)) * (l - 1) if l > 1 else 0


def block_len(block_num):
    """Длина блока (т. е. строки '1234567891011...str(block_num)'"""
    l = len(str(block_num))
    return len_sum(l) + (block_num - 10 ** (l - 1) + 1) * l


def arith_sum(n):
    return n * (n + 1) // 2


def block_len_sum(block_num):
    """Суммарная длина всех блоков подряд вплоть до блока block_num
    Если l = len(str(block_num))
    """
    l = len(str(block_num))
    result = 0
    for i in range(1, l + 1):
        # прибавляем суммарную длину блоков, заканчивающихся на числа длины i
        ls = len_sum(i)  # длина блока для числа 10 ** i - 1
        if i < l:
            ln = len_num(i)
        else:
            ln = block_num - (10 ** (l - 1)) + 1
        result += ls * ln + i * arith_sum(ln)
    return result


def block(n):
    return ''.join(str(i) for i in range(1, n + 1))


def blocks(n):
    return ''.join(block(i) for i in range(1, n + 1))


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
