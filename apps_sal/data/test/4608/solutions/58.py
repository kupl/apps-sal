n = int(input())
a = [0] * n
for i in range(n):
    a[i] = int(input())
visit = set()
now = 1
for i in range(1, n + 10):
    if now not in visit:
        visit.add(now)
        now = a[now - 1]
    else:
        print(-1)
        break
    if now == 2:
        print(i)
        break
