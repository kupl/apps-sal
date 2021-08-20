(a, b, k) = map(int, input().split())
if k <= a:
    a -= k
elif k <= a + b:
    (a, b) = (0, b - (k - a))
else:
    (a, b) = (0, 0)
print(a, b)
