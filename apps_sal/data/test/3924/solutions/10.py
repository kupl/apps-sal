n, m = map(int, input().split())

a = list(map(int, input().split()))

res = 0
sum = 0
can = True

for i in range(n):
    if sum > 0:
        sum = sum + a[i]
        if sum < m:
            res = res + 1
            sum = 0
        else:
            res = res + sum // m
            sum = sum % m
    else:
        sum = sum + a[i]
        res = res + sum // m
        sum = sum % m

if sum > 0:
    res = res + 1
print(res)
