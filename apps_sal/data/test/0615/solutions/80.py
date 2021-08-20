def main():
    N = int(input())
    A = list(map(int, input().split(' ')))
    X = [0 for _ in range(N + 1)]
    for i in range(N):
        X[i + 1] = X[i] + A[i]
    ans = 10 ** 10
    left = 0
    right = 2
    for i in range(1, N):
        while left < i:
            d = abs(X[left] - (X[i] - X[left]))
            d_next = abs(X[left + 1] - (X[i] - X[left + 1]))
            if d_next > d:
                break
            left += 1
        while right < N:
            d = abs(X[N] - X[right] - (X[right] - X[i]))
            d_next = abs(X[N] - X[right + 1] - (X[right + 1] - X[i]))
            if d_next > d:
                break
            right += 1
        (p, q, r, s) = (X[left], X[i] - X[left], X[right] - X[i], X[N] - X[right])
        ans = min([ans, max([p, q, r, s]) - min([p, q, r, s])])
    print(ans)


def __starting_point():
    main()


__starting_point()
