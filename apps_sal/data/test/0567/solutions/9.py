n = int(input())
a = list(map(int, input().split()))
res = min(a[-1] - 1, 10**6 - a[0])


for i in range(n - 1):
    res = min(res, max(a[i] - 1, (10**6 - a[i + 1])))
print(res)
