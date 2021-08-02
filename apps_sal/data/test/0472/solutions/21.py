import math
c = int(input())
f = False
for b in range(82):
    x = [(-b + math.sqrt(b**2 + (4 * c))) / 2, (-b - math.sqrt(b**2 + (4 * c))) / 2]
    x = max(x)

    if int(x)**2 + b * int(x) - c == 0 and int(x) == x:
        y = 0
        for i in str(int(x)):
            y += int(i)
        if b == y:
            print(int(x))
            f = True

if f == False:
    print(-1)
