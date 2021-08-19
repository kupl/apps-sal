(a, b, k) = map(int, input().split())
if k < a:
    a -= k
elif k < a + b:
    b = b - k + a
    a = 0
else:
    a = 0
    b = 0
print(a, b)
