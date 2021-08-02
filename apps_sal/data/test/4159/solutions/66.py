a, b, k = [int(i) for i in input().split()]
if a <= k:
    b = b - k + a if b - k + a >= 0 else 0
    a = 0
else:
    a -= k
print(a, b)
