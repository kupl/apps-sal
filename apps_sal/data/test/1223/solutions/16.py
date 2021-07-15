n = int(input())
p = list(map(int, input().split()))
lis = [0] * (n + 1)
for i in range(n):
    lis[p[i]] = i
l = list(range(-1, n - 1)) + [-1, -1]
r = list(range(1, n + 1)) + [n, n]
ans = 0
for i in range(n):
    ans += (i + 1) * ((lis[i + 1] - l[lis[i + 1]]) * (r[r[lis[i + 1]]] - r[lis[i + 1]]) + (l[lis[i + 1]] - l[l[lis[i + 1]]]) * (r[lis[i + 1]] - lis[i + 1]))
    r[l[lis[i + 1]]] = r[lis[i + 1]]
    l[r[lis[i + 1]]] = l[lis[i + 1]]
print(ans)
