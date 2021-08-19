(n, k) = map(int, input().split())
td = [list(map(int, input().split())) for i in range(n)]
td.sort(key=lambda x: x[1], reverse=True)
a = 0
ans = []
kind = [-1] * n
c = 0
min_p = []
for i in range(n):
    eat = False
    if i < k:
        a += td[i][1]
        eat = True
    elif min_p:
        if kind[td[i][0] - 1] < 0:
            a -= min_p.pop() - td[i][1]
            a += (c + 1) ** 2 - c ** 2
            ans.append(a)
            eat = True
    if eat:
        if kind[td[i][0] - 1] < 0:
            kind[td[i][0] - 1] = 1
            c += 1
        else:
            min_p.append(td[i][1])
    if i == k - 1:
        a += c ** 2
        ans.append(a)
print(max(ans))
