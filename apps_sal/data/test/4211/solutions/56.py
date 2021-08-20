n = int(input())
a = [int(x) for x in input().split()]
res = [0] * n
res[0] = a[0]
for i in range(1, n - 1):
    res[i] = min(a[i], a[i - 1])
res[n - 1] = a[-1]
print(sum(res))
