n, k = [int(x) for x in input().split()]
h = [int(x) for x in input().split()]
s = sum(h[: k])
res = s
pos = 0
for i in range(n - k):
    s += h[i + k] - h[i]
    if s < res:
        res = s
        pos = i + 1
print(pos + 1)
