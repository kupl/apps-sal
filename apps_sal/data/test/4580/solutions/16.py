n = int(input())
a = list(map(int, input().split()))
a1 = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
ans = 0
for i in range(n):
    if 1 <= a[i] <= 399:
        a1 = 1
    elif 400 <= a[i] <= 799:
        b = 1
    elif 800 <= a[i] <= 1199:
        c = 1
    elif 1200 <= a[i] <= 1599:
        d = 1
    elif 1600 <= a[i] <= 1999:
        e = 1
    elif 2000 <= a[i] <= 2399:
        f = 1
    elif 2400 <= a[i] <= 2799:
        g = 1
    elif 2800 <= a[i] <= 3199:
        h = 1
    else:
        ans += 1
x = a1 + b + c + d + e + f + g + h
if a1 == b == c == d == e == f == g == h == 0:
    print(1, ans)
else:
    print(x, x + ans)
