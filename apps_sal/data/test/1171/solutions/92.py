(N, K) = map(int, input().split())
V = list(map(int, input().split()))
MAX = 0
for k in range(1, K + 1):
    for ka in range(k + 1):
        for kb in range(k + 1 - ka):
            kcd = k - ka - kb
            if ka + kb <= kcd or ka + kb > N:
                continue
            s = V[:ka] + V[-kb:] if kb != 0 else V[:ka]
            s.sort()
            MAX = max(MAX, sum(s[kcd:]))
print(MAX)
