from itertools import accumulate


def main():
    (N, K) = list(map(int, input().split()))
    A = list(map(int, input().split()))
    A.sort()
    p = 10 ** 9 + 7
    if K == 1:
        print(0)
        return
    a = [None] * (N + 1)
    inva = [None] * (N + 1)
    a[0] = 1
    for i in range(1, N + 1):
        a[i] = i * a[i - 1] % p
    inva[N] = pow(a[N], p - 2, p)
    for i in range(N):
        inva[N - i - 1] = inva[N - i] * (N - i) % p
    ans = 0
    maxA = list(accumulate(A[::-1]))
    minA = list(accumulate(A))
    for i in range(K - 1, N):
        j = min(i, N - i)
        tmp = a[i - 1] * inva[K - 2] % p * inva[i - K + 1] % p
        ans += (maxA[j - 1] - minA[j - 1]) * tmp % p
        ans %= p
    print(ans)


def __starting_point():
    main()


__starting_point()
