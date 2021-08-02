n = int(input())
a = [int(x) for x in input().split()]
a.sort(reverse=True)
res = 0
for i in range(n):
    if i % 2 == 0:
        res += a[i]
    else:
        res -= a[i]
print(res)
