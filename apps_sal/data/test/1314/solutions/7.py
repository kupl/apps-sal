n = int(input())
maxX = -10000000000
maxY = -10000000000
minA = 10000000000
minB = 10000000000
for i in range(n):
    (a, b) = list(map(int, input().split()))
    if a > maxX:
        maxX = a
    if b > maxY:
        maxY = b
for i in range(n):
    (a, b) = list(map(int, input().split()))
    if a < minA:
        minA = a
    if b < minB:
        minB = b
print(maxX + minA, maxY + minB)
