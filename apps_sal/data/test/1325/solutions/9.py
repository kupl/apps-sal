(n, p) = map(int, input().split())
t = input()
k = n // 2
d = [0] * (k + 1)
for i in range(k):
    d[i] = abs(ord(t[i]) - ord(t[n - i - 1]))
    if 2 * d[i] > 26:
        d[i] = 26 - d[i]
p = n - p if p > k else p - 1
if d.count(0) == k + 1:
    print(0)
else:
    (i, j) = (0, k)
    while d[i] == 0:
        i += 1
    while d[j] == 0:
        j -= 1
    if i > p:
        i = p
    if j < p:
        j = p
    print(sum(d) + min(p - 2 * i + j, 2 * j - i - p))
