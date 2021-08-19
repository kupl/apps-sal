n = int(input())
a = [0] * n
for i in range(n):
    a[i] = int(input())
counter = 0
now = 1
visit = [False] * n
visit[0] = True
while True:
    counter += 1
    if a[now - 1] == 2:
        print(counter)
        break
    elif visit[a[now - 1] - 1] == True:
        print(-1)
        break
    else:
        visit[a[now - 1] - 1] = True
    now = a[now - 1]
