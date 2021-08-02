n = int(input())
p = list(map(int, input().split()))
l = [0] + [i for i in range(n + 1)]
r = [i + 1 for i in range(n + 1)] + [n + 1]
d = [0] * (n + 1)
for i in range(n):
    d[p[i]] = i + 1
ans = 0
for i in range(1, n + 1):
    ans += ((r[r[d[i]]] - r[d[i]]) * (d[i] - l[d[i]]) + (r[d[i]] - d[i]) * (l[d[i]] - l[l[d[i]]])) * i
    l[r[d[i]]], r[l[d[i]]] = l[d[i]], r[d[i]]
print(ans)
