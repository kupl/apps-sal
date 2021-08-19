# https://codeforces.com/contest/1054/problem/D
n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
p = [0] * (n + 1)
base = (1 << k) - 1


def kC2(k):
    return (k - 1) * k // 2


d = {}
for i in range(1, n + 1):
    p[i] = p[i - 1] ^ a[i - 1]
    p[i] = min(p[i], p[i] ^ base)

    if p[i] not in d:
        d[p[i]] = 0
    d[p[i]] += 1

if 0 not in d:
    d[0] = 0
d[0] += 1

ans = n * (n + 1) // 2
minus = 0

for k, v in list(d.items()):
    minus += kC2(v // 2) + kC2(v - v // 2)

print(ans - minus)

# 6 3
# 1 4 4 7 3 4
