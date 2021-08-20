n = int(input())
a = [int(x) for x in input().split()]
res = 0
c = 0
for i in range(n - 1):
    if a[i] >= a[i + 1]:
        c += 1
    else:
        res = max(res, c)
        c = 0
res = max(res, c)
print(res)
