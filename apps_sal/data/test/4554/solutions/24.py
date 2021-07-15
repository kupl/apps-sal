w, a, b = list(map(int, input().split()))
if b + w < a:
    res = a - (b + w)
elif a <= b + w <= a + 2 * w:
    res = 0
else:
    res = b - (a + w)

print(res)

