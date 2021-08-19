import sys
(n, x) = map(int, input().split())
sad = 0
for i in range(n):
    (a, b) = map(str, input().split())
    b = int(b)
    if a == '+':
        x += b
    elif x >= b:
        x -= b
    else:
        sad += 1
print(x, sad)
