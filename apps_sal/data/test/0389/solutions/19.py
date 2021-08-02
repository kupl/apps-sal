a, b = list(map(int, input().split()))

a2 = 0
a3 = 0
a5 = 0
b2 = 0
b3 = 0
b5 = 0

while a % 2 == 0:
    a //= 2
    a2 += 1
while a % 3 == 0:
    a //= 3
    a3 += 1
while a % 5 == 0:
    a //= 5
    a5 += 1
while b % 2 == 0:
    b //= 2
    b2 += 1
while b % 3 == 0:
    b //= 3
    b3 += 1
while b % 5 == 0:
    b //= 5
    b5 += 1

tot = max(a2 - min(a2, b2), b2 - min(a2, b2)) + max(a3 - min(a3, b3), b3 - min(a3, b3)) + max(a5 - min(a5, b5), b5 - min(a5, b5))
if a == b:
    print(tot)
else: print(-1)
