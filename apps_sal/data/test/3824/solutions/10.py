a, b = input().split()
a, b = int(a), int(b)
c, d = input().split()
c, d = int(c), int(d)

if abs(a - c) == 0:
    print(2 * abs(b - d) + 6)
elif abs(b - d) == 0:
    print(2 * abs(a - c) + 6)
else:
    print(2 * abs(a - c) + 2 * abs(b - d) + 4)
