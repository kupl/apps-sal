n, k = [int(x) for x in input().strip().split()]
a = [int(x) for x in input().strip().split()]
initsum = sum(a[:k])
allsum = initsum
for i in range(k, n):
    initsum -= a[i-k]
    initsum += a[i]
    allsum += initsum
print(allsum/(n-k+1))

