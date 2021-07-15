a, b, c, d = map(int, input().split())

if c % b == 0:
    t = c / b
else:
    t = (c // b) + 1

if a % d == 0:
    o = a / d
else:
    o = (a // d) + 1

if t > o:
    print("No")
elif t <= o:
    print("Yes")
