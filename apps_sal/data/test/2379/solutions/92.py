def main():
    import sys
    def input(): return sys.stdin.readline().rstrip()
    n, k, c = list(map(int, input().split()))
    s = [True if i == 'o' else False for i in input()]
    L = [0] * k
    R = [0] * k
    i = n - 1
    now = k - 1
    while 0 <= now:
        if s[i]:
            R[now] = i
            i -= c
            now -= 1
        i -= 1
    i = 0
    now = 0
    while now < k:
        if s[i]:
            L[now] = i
            if L[now] == R[now]:
                print((i + 1))
            i += c
            now += 1
        i += 1


def __starting_point():
    main()


__starting_point()
