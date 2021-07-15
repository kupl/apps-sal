a, b, k = map(int, input().split())
if a < k and k <= a + b:
    k = k - a
    a = 0
    b = b - k
elif a + b < k:
    a = 0
    b= 0
else:
    a = a - k

print(a , b)
