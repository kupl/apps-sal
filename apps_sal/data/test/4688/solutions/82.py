(n, k) = [int(x) for x in input().split()]
res = k
for i in range(1, n):
    res *= k - 1
print(res)
