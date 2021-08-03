a, b, k = [int(x) for x in input().split()]
res = b // k
res -= (a - 1) // k
print(res)
