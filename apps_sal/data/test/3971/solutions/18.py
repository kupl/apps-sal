n = int(input())
a = [int(x) for x in input().split()]
x = [0] * 100001
dp = [0]
for i in range(n):
    x[a[i]] += 1
dp.append(x[1])
for i in range(2, 100001):
    dp.append(max(dp[-1], dp[-2] + x[i] * i))
print(dp[-1])
