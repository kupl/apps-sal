n = int(input())
t = list(map(int, input().split()))
(s, k) = (0, 5001)
d = [0, 0] * k
for a in t:
    for b in t:
        d[b - a] += 1
for i in range(k, 2 * k):
    d[i] += d[i - 1]
for i in range(1, k):
    s += d[i] * sum((d[j] * d[-1 - i - j] for j in range(1, k - i)))
print(8 * s / (n * n - n) ** 3)
