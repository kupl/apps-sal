n = int(input())
a = 0
b = 0
for i in range(n):
    (x, y) = list(map(str, input().split()))
    if y == 'soft':
        a += 1
    else:
        b += 1
c = max(a, b)
if a % 2 == 1 and b % 2 == 1 and (a == b):
    c = a + 1
for i in range(1000):
    kol = (i * i + 1) / 2
    if kol >= c:
        print(i)
        break
