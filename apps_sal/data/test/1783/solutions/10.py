n, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
total = sum(a[:k])
res = total
for i in range(1, n-k+1):
    total += - a[i-1] + a[i+k-1]
    res += total
print(res/(n-k+1))
