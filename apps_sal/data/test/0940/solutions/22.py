n = input().split()
a = int(n[0])
b = int(n[1])
c = int(n[2])
if a >= b + c:
    print(a - b - c + 1)
elif b >= a + c:
    print(b - a - c + 1)
elif c >= a + b:
    print(c - a - b + 1)
else:
    print(0)
