x, y = list(map(int, input().split()))
if (x > y):
    x, y = y, x
a = x
b = x
c = x
ans = 0
while not (a == b == c == y):
    if (a <= b and a <= c):
        a = min(b + c - 1, y)
    elif (b <= a and b <= c):
        b = min(a + c - 1, y)
    elif (c <= a and c <= b):
        c = min(a + b - 1, y)
    ans += 1
print(ans)
