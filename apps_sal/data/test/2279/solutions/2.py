n = int(input())
p = [-1] * 2 * n
k = []
for i in range(2 * n - 1):
    a = list(map(int, input().split()))
    for t in range(i + 1):
        k.append([a[t], i + 1, t])
k.sort()
for i in range(len(k) - 1, -1, -1):
    if p[k[i][1]] == -1 and p[k[i][2]] == -1:
        p[k[i][1]] = k[i][2] + 1
        p[k[i][2]] = k[i][1] + 1
print(*p)
