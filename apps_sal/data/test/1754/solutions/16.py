n, m, k = map(int, input().split())
p = list(map(int, input().split()))
s = list(map(int, input().split()))
c = list(map(int, input().split()))
lst = []
ans = 0
for i in range(m):
    lst.append([])
for i in range(n):
    lst[s[i] - 1].append((p[i], i))
for i in range(m):
    lst[i].sort()
    lst[i] = lst[i][-1::-1]

    cnt = 0
    for j in range(1, len(lst[i])):
        if lst[i][j][1] + 1 in c:
            ans += 1
print(ans)
