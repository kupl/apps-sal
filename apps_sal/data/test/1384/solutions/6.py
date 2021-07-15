

def solve(s):
    '''
    >>> solve([1, 1, 0, 1])
    3
    >>> solve([0, 1, 0, 0, 1, 0])
    4
    >>> solve([0])
    1
    '''
    zeroes = accum(s, 0)
    ones = list(reversed(accum(reversed(s), 1)))
    return max(x + y for x, y in zip(zeroes, ones))


def accum(lst, value):
    counts = [0]
    for el in lst:
        if el == value:
            counts.append(counts[-1] + 1)
        else:
            counts.append(counts[-1])
    return counts


def main():
    n = input()
    s = list(map(int, input().split()))
    print(solve(s))


def __starting_point():
    main()

__starting_point()
