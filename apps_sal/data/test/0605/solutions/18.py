p = input().split()

a = int(p[0])
b = int(p[1])
c = int(p[2])
d = int(p[3])

ms = max(a * 3 // 10, (a - (a // 250) * c))

vs = max(b * 3 // 10, (b - (b // 250) * d))

if ms > vs:
    print("Misha")
elif vs > ms:
    print("Vasya")
else:
    print("Tie")
