n, p = list(map(int, input().split()))
a = [input() for i in range(n)]
cur = 1
cnt = 1
for i in a[-2::-1]:
    if i == 'halfplus':
        cur = cur * 2 + 1
        cnt += cur
    else:
        cur *= 2
        cnt += cur
print(cnt * p // 2)

