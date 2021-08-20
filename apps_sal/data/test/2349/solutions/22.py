def sp():
    return list(map(int, input().split()))


def si():
    return int(input())


TESTCASES = int(input())
for tc in range(TESTCASES):
    n = si()
    ints = set(range(int(n ** 0.5) + 1))
    for i in range(int(n ** 0.5) + 1, 0, -1):
        ints.add(n // i)
    ints = sorted(list(ints))
    print(len(ints))
    print(' '.join(map(str, ints)))
