n, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
res = 0
for i in range(n):
    if k <= a[i]:
        res += 1
print(res)
