import math

n = int(input())

a = [0 for t in range(2, 2001)]
b = [0 for t in range(-999, +1000)]
for i in range(n):
    x, y = [int(t) for t in input().split()]

    a[x+y-2] += 1
    b[x-y+999] += 1

ans = 0
for pos in a:
    if pos > 1:
        head = math.factorial(pos)
        tail = 2*math.factorial(pos-2)
        ans += int(head/tail)

for pos in b:
    if pos > 1:
        head = math.factorial(pos)
        tail = 2*math.factorial(pos-2)
        ans += int(head/tail)

print(int(ans))

