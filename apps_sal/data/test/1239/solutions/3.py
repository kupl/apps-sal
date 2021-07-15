n = int(input())
a = list(map(int, input().split()))
a.sort()
minm = 10000000000
mincount = 0
for i in range(n - 1):
    if a[i + 1] - a[i] == minm:
        mincount += 1
    elif a[i + 1] - a[i] < minm:
        minm = a[i + 1] - a[i]
        mincount = 1
print(minm, mincount)
