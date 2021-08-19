n = int(input())
a = []
for _ in range(n):
    (ai, bi) = list(map(int, input().split()))
    a.append((ai, bi, ai - bi))
a.sort(key=lambda x: x[2], reverse=True)
s = 0
for (i, k) in enumerate(a):
    s += k[0] * i + k[1] * (n - i - 1)
print(s)
