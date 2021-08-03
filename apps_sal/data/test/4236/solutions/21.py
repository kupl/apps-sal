
s = input().split(" ")
n, m = int(s[0]), int(s[1])
visit = [0 for i in range(m + 1)]
for i in range(n):
    s = input().split(" ")
    l, r = int(s[0]), int(s[1])
    for i in range(l, r + 1):
        visit[i] = 1
res = []
for i in range(1, m + 1):
    if visit[i] == 0:
        res.append(i)
print(len(res))
for i in res:
    print(i, end=" ")
