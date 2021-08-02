n, a, b = [int(x) for x in input().split()]
mxmn = max(min(a // i, b // (n - i)) for i in range(1, n))
print(mxmn)
