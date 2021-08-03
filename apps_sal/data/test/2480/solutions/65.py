from collections import Counter


def solve():
    ans = 0
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    cum = [0] * (N + 1)
    for i in range(N):
        cum[i + 1] = (cum[i] + A[i]) % K
    for i in range(N):
        cum[i + 1] = (i + 1 - cum[i + 1]) % K
    if N < K:
        c = Counter(cum)
        for v in c.values():
            ans += v * (v - 1) // 2
    else:
        c = Counter(cum[:K - 1])
        for i in range(N):
            c[cum[i]] -= 1
            if i + K - 1 <= N:
                c[cum[i + K - 1]] += 1
            ans += c[cum[i]]
    return ans


print(solve())
