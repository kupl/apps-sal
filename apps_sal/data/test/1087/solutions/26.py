(n, K) = list(map(int, input().split()))
a = list(map(int, input().split()))
c = [0] * 40
ans = 0
for aa in a:
    for k in range(40):
        if aa & 1 << k:
            c[k] += 1
x = 0
for k in range(39, -1, -1):
    if x + (1 << k) > K:
        continue
    if c[k] <= n - c[k]:
        x += 1 << k
for aa in a:
    ans += x ^ aa
print(ans)
