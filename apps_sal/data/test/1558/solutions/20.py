(n, r, avg) = list(map(int, input().split()))
a = []
sum = int(round(avg * n))
sum1 = 0
res = 0
for i in range(n):
    (x, y) = list(map(int, input().split()))
    a.append([y, x])
    sum1 += x
a.sort()
i = 0
while sum > sum1:
    if sum - sum1 > r - a[i][1]:
        sum1 += r - a[i][1]
        res += (r - a[i][1]) * a[i][0]
        i += 1
    else:
        res += (sum - sum1) * a[i][0]
        sum1 = sum
print(res)
