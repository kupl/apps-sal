def solve():
    ans = 0
    N, K = list(map(int, input().split()))
    V = list(map(int, input().split()))
    A = V[:] * 2
    for k in range(K, -1, -1):
        if k >= N:
            suteru = k - N
            a = V[:]
            a.sort()
            ans = max(ans, sum(a[suteru:]))
        else:
            for i in range(k // 2 + 1, k + 1):
                suteru = k - i
                for j in range(i + 1):
                    a = A[N - j:N + i - j]
                    a.sort()
                    ans = max(ans, sum(a[suteru:]))
    return ans


print((solve()))
