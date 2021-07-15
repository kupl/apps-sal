lst = input().split()

a = int(lst[0])
b = int(lst[1])
x = int(lst[2])

if a % x != 0:
   a = x * ((a // x) + 1)

if b % x != 0:
   b = x * (b // x)

print(((b - a) // x) + 1)
