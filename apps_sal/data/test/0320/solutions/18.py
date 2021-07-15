def readln(): return tuple(map(int, input().split()))

n, = readln()
a = b = c = 0
for _ in range(n):
    x, y = readln()
    a += x
    b += y
    c += (x % 2) ^ (y % 2)
if a % 2 == 0 and b % 2 == 0:
    print(0)
elif (a % 2) == (b % 2) and c:
    print(1)
else:
    print(-1)

