def check(x, N, S):
    candidate = set()
    for i in range(N - 2 * x + 1):
        candidate.add(S[i:i + x])
        if S[i + x:i + 2 * x] in candidate:
            return True
    return False


def main():
    n = int(input())
    s = input().rstrip()
    l = 0
    r = n
    while l < r:
        mid = (l + r + 1) // 2
        if check(mid, n, s):
            l = mid
        else:
            r = mid - 1
    print((l + r + 1) // 2)


def __starting_point():
    main()


__starting_point()
