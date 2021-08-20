line = input().split()
line.sort()
(a, b, c) = line
if a == b and a == c:
    print(0)
elif a == b:
    print(1)
elif b == c:
    print(1)
elif a[1] == b[1] and b[1] == c[1] and (int(b[0]) - int(a[0]) == 1) and (int(c[0]) - int(b[0]) == 1):
    print(0)
elif a[1] == b[1] and int(b[0]) - int(a[0]) in [1, 2]:
    print(1)
elif b[1] == c[1] and int(c[0]) - int(b[0]) in [1, 2]:
    print(1)
elif a[1] == c[1] and int(c[0]) - int(a[0]) in [1, 2]:
    print(1)
else:
    print(2)
