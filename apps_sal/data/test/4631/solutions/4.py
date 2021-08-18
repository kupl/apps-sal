from collections import deque

n, m = list(map(int, input().split()))

x = list(map(int, input().split()))

dic = {}
q = deque([])

d = 0
ans = []

for i in range(n):

    dic[x[i]] = 1

for i in range(n):

    if x[i] - 1 not in dic:
        dic[x[i] - 1] = 1
        q.append([x[i] - 1, 1, "l"])
    if x[i] + 1 not in dic:
        dic[x[i] + 1] = 1
        q.append([x[i] + 1, 1, "r"])

for i in range(m):

    now = q.popleft()

    p = now[0]
    d += now[1]
    direc = now[2]

    ans.append(p)

    if direc == "l":
        if p - 1 not in dic:
            dic[p - 1] = 1
            q.append([p - 1, now[1] + 1, direc])
    else:
        if p + 1 not in dic:
            dic[p + 1] = 1
            q.append([p + 1, now[1] + 1, direc])

print(d)
print(" ".join(map(str, ans)))
