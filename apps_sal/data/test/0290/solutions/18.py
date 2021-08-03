def sq(x):
    s = int(x**0.5)
    for i in range(1, -2, -1):
        ts = s + i
        if ts**2 <= x:
            return ts


n = int(input())
s = sq(n)

if s**2 == n:
    print(s * 2)
elif (s + 1) * s >= n:
    print(s * 2 + 1)
else:
    print(s * 2 + 2)
