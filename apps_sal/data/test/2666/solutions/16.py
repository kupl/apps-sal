(n, k) = list(map(int, input().split()))
k = k // 2
l = []
d = {}
for i in range(n):
    l.append(int(input()))
for i in range(k + 1):
    d[i] = [0] * n
for i in range(1, k + 1):
    maxdiff = d[i - 1][0] - l[0]
    for j in range(1, n):
        maxdiff = max(d[i - 1][j] - l[j], maxdiff)
        d[i][j] = max(d[i][j - 1], maxdiff + l[j])
print(d[k][-1])
