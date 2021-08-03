from math import log


n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))

ans = 0
a = [[] for i in range(200001)]
for i in range(n):
    x = arr[i]
    l = 0
    while True:
        a[x].append(l)
        if x == 0:
            break
        x //= 2
        l += 1
mn = 1000000000
for i in range(len(a)):
    a[i].sort()
    if len(a[i]) >= k:
        mn = min(mn, sum(a[i][:k]))
print(mn)
