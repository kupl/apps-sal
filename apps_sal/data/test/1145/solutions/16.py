n = int(input())
a = [int(x) for x in input().split()]
a.sort()
res = 0
last_upd = 0
for i in range(1, n):
    if a[i] <= a[i - 1]:
        res += a[i - 1] + 1 - a[i]
        a[i] = a[i - 1] + 1
print(res)
