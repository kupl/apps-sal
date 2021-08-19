def main():
    (n, k, p, x, y) = list(map(int, input().split()))
    L = list(map(int, input().split()))
    [L.append(y) for _ in range(n - k)]
    cnt = 0
    for i in range(n):
        if L[i] >= y:
            cnt += 1
    m = (n + 1) / 2
    for i in range(k, n):
        if cnt > m:
            L[i] = 1
            cnt -= 1
    if sum(L) > x or cnt < m:
        print(-1)
    else:
        print(' '.join(map(str, L[k:])))


def __starting_point():
    main()


__starting_point()
