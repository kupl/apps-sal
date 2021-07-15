n = int(input())
a = [int(x) for x in input().split()]
a.sort()
z = []
res = 0
for i in range(n-1):
    while a[i+1] <= a[i]:
        a[i+1] += 1
        res += 1
print(res)

