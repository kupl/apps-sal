a = int(input())

b = int(input())

dist = abs(b - a)

d1 = dist // 2

d2 = dist - d1

u1 = (d1 + 1) * d1 // 2

u2 = (d2 + 1) * d2 // 2 

print(u1 + u2)
