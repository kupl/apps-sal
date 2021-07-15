a, b, c = list(map(int, input().split()))
x = max(a, b, c)
a = x - a
b = x - b
c = x - c
if (a > 0 and b > 0) or (a > 0 and c > 0) or (b > 0 and c > 0):
    print(a + b + c - 2)
elif a > 0 or b > 0 or c > 0:
    print(a + b + c - 1)
else:
    print(a + b + c)
