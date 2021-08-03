n, d = list(map(int, input().split()))
t = list(map(int, input().split()))

tot = sum(t)
limit = tot + (n - 1) * 10

rest = d - limit

c = 0
# print(rest)
if limit > d:
    print(-1)
else:
    for i in range(n - 1):
        c += 2

    c += (rest // 5)

    print(c)
