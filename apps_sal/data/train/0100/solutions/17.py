def sp():
    return list(map(int, input().split()))


def si():
    return int(input())


TESTCASES = int(input())
for tc in range(TESTCASES):
    (r, g, b) = sorted(sp())
    if b > r + g:
        b = r + g
    print((r + g + b) // 2)
