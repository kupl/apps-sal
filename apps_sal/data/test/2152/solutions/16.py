n = int(input())

a = []
p = []
dp = []

for i in range(n):
    cur1, cur2 = map(int, input().split())
    a.append(cur1)
    p.append(cur2)

dp.append(p[0])
sum = p[0] * a[0]

for i in range(1, n):
    if p[i] >= dp[-1]:
        dp.append(dp[-1])
    else:
        dp.append(p[i])
    sum += dp[-1] * a[i]

print(sum)
