from fractions import *
n = int(input())
s = n * (n - 1) * (n - 2) // 6
p = [list(map(int, input().split()))for _ in range(n)]
for i in range(n):
    k, l = 0, sorted(1e9 if p[i][1] == Y else (p[i][0] - X) / (p[i][1] - Y)for X, Y in p[:i])
    for j in range(1, i):
        k = k + 1 if l[j] == l[j - 1]else 0
        s -= k
print(s)
