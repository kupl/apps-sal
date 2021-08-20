(n, m, k) = map(int, input().split())
chats = list()
for i in range(m):
    chats.append([set(), 0])
emps = [0] * n
for i in range(n):
    e = list(map(int, input().split()))
    for j in range(m):
        if e[j] == 1:
            chats[j][0].add(i)
for i in range(k):
    (x, y) = map(int, input().split())
    x -= 1
    y -= 1
    chats[y][1] += 1
    emps[x] -= 1
for i in chats:
    for j in i[0]:
        emps[j] += i[1]
for i in range(n):
    print(emps[i], end=' ')
