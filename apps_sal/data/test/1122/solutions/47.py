def main():
    N, M = list(map(int, input().split()))
    ans = list()
    if N % 2 == 1:
        for k in range(min(N // 2, M)):
            ans.append((k + 1, N - k))
    else:
        K = N // 2 - 1
        for k in range((K + 1) // 2):
            if len(ans) >= M:
                break
            ans.append((k + 1, N - k))
        for k in range(K // 2):
            if len(ans) >= M:
                break
            b = N - (K + 1) // 2 - k
            a = b - 2 * (K // 2 - k)
            ans.append((a, b))
    for row in ans:
        print(('{} {}'.format(row[0], row[1])))


def __starting_point():
    main()

__starting_point()
