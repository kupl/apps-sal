n = int(input())
t = sorted(map(int, input().split()))
m = 5001
d = [0, 0] * m
for a in t:
    for b in t: d[b - a] += 1
for i in range(m, 2 * m): d[i] = d[i - 1] + d[i]
s = 0
for i in range(1, m):
    s += d[i] * sum(d[j] * d[-1 - i - j] for j in range(1, m - i))
print(8 * s / (n * n - n) ** 3)
