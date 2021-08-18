import math

n = int(input())
a = int(input())
b = int(input())

#print( n, a, b )

MAXVAL = 10000000

x = 0

while a * x <= n:

    if (n - x * a) % b == 0:
        print("YES")
        print(x, (n - x * a) // b)
        return

    x += 1

print("NO")
