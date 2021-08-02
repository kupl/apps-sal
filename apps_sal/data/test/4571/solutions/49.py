a = [int(s) for s in input().split()]
print(((a[0] - a[1]) * 100 + a[1] * 1900) * (2**a[1]))
