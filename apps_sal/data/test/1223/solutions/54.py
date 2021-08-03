n = int(input())
p = list(map(int, input().split()))
ind = [0] * n
for i in range(n):
    ind[p[i] - 1] = i + 1
l = [0] + [i for i in range(n + 1)]
r = [i + 1 for i in range(n + 1)] + [n + 1]
ans = 0
for i in range(n):
    ans += (r[r[ind[i]]] - r[ind[i]]) * (ind[i] - l[ind[i]]) * (i + 1)
    ans += (l[ind[i]] - l[l[ind[i]]]) * (r[ind[i]] - ind[i]) * (i + 1)
    l[r[ind[i]]], r[l[ind[i]]] = l[ind[i]], r[ind[i]]
print(ans)
