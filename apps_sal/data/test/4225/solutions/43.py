a, b, c, k = list(map(int, input().split()))
if k <= a:
    res = k
elif k <= a + b:
    res = a
else:
    res = a - (k - a - b)
print(res)
