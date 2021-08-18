visit = dict()
exist = dict()
n = int(input())
x = sorted(map(int, input().split()))
limit = max(x)
for n, i in enumerate(x):
    exist[i] = n + 1
ans, ans2 = 1, [x[0]]
for i in range(len(x)):
    if visit.get(x[i], 0):
        continue
    j = 1
    while x[i] + j <= limit:
        visit[x[i] + j] = True
        if exist.get(x[i] + j, 0):
            if ans == 1:
                ans = 2
                ans2 = [x[i], x[i] + j]
            if j != 1 and exist.get(x[i] + j // 2, 0):
                print(3)
                print(x[i] + j, x[i], x[i] + j // 2)
                return
        j *= 2

if ans == 2:
    print(2)
    print(ans2[0], ans2[1])
else:
    print(1)
    print(x[0])
