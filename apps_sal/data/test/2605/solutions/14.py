n, k = list(map(int, input().split()))
c = list(map(int, input().split()))
d = set(map(int, input().split()))

s = 0
s0 = sum(c)

for i in d:
    s0 -= c[i - 1]
    s += s0 * c[i - 1]

for i in range(n):
    if i + 1 not in d and (i + 1) % n + 1 not in d:
        s += c[i] * c[(i + 1) % n]

print(s)
