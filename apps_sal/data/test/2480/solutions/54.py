from collections import defaultdict

N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

Am = [a - 1 for a in A]
Acc = [0] * (N + 1)
for i in range(N):
    Acc[i + 1] = (Acc[i] + Am[i]) % K

d = defaultdict(int)
l, r = 0, 0
ans = 0
while r <= N:
    a = Acc[r]
    ans += d[a]
    d[a] += 1
    r += 1
    if r - l >= K:
        d[Acc[l]] -= 1
        l += 1
print(ans)
