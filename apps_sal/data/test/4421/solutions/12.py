n, k = list(map(int, input().split()))
l = list(map(int, input().split()))

d = {}

for i in range(k):
    d[i] = 0

for i in range(len(l)):
    l[i] = l[i] % k
    d[l[i]] += 1

s = 0

s += d[0] // 2

for i in range(1, k // 2):
    s += min(d[i], d[k - i])

if k % 2 == 0:
    s += d[k // 2] // 2
else:
    if k != 1:
        s += min(d[k // 2], d[k - k // 2])

print(s * 2)
