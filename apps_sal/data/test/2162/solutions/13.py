(k1, k2, k3) = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
a = sorted(a)
b = sorted(b)
c = sorted(c)
n = k1 + k2 + k3
l = [0] * (n + 1)
r = [0] * (n + 1)
p = 0
for i in range(n + 1):
    if p < len(a) and i == a[p]:
        p += 1
    l[i] += len(a) - p
p = 0
for i in range(n + 1):
    if p < len(b) and i == b[p]:
        p += 1
    l[i] += p
p = 0
for i in range(n + 1):
    if p < len(b) and i == b[p]:
        p += 1
    r[i] += len(b) - p
p = 0
for i in range(n + 1):
    if p < len(c) and i == c[p]:
        p += 1
    r[i] += p
r_cum_min = [None] * (n + 1)
r_cum_min[-1] = r[n]
i = n - 1
while i >= 0:
    r_cum_min[i] = min(r[i], r_cum_min[i + 1])
    i -= 1
answer = 1000000000.0
for i in range(n + 1):
    if l[i] + r_cum_min[i] < answer:
        answer = l[i] + r_cum_min[i]
print(answer)
