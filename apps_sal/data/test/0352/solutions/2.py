n = int(input())
a1, a2 = list(map(int, input().split()))
b1, b2 = list(map(int, input().split()))
c1, c2 = list(map(int, input().split()))

a = a1
b = b1
c = c1
s = a + b + c

if a2 - a1 < n - s:
    a = a2
    s += a2 - a1
    if b2 - b1 < n - s:
        b = b2
        s += b2 - b1
        if c2 - c1 < n - s:
            c = c2
        else:
            c += n - s
    else:
        b += n - s
else:
    a += n - s

print(a, b, c)
