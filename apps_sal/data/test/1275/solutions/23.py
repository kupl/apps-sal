import sys


def LI():
    return list(map(int, input().split()))


N, K = LI()
K = abs(K)
ans = 0

for i in range(2 + K, 2 * N + 1):
    i -= 1
    L = max(0, (i - N) * 2)
    R = max(0, (i - K - N) * 2)
    ans += (i - L) * (i - K - R)
print(ans)
