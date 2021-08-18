import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

n = int(input())
a = [int(x) for x in input().split()]
[r1, c1, r2, c2] = [int(x) for x in input().split()]

r1 -= 1
r2 -= 1
c1 -= 1
c2 -= 1

dr = r2 - r1
ddr = dr // abs(dr) if dr != 0 else 1

c = c1

for i in range(abs(dr) + 1):
    r = r1 + ddr * i
    c = min(c, a[r])

pen1 = 0
for i in range(min(r1, r2)):
    pen = (min(r1, r2) - i) * 2
    if c > c2 and a[i] < c and a[i] <= min(a[i:min(r1, r2)]):
        pen -= c - c2 - abs(a[i] - c2)
    pen1 = min(pen1, pen)

pen2 = 0
for i in range(max(r1, r2) + 1, n):
    pen = (i - max(r1, r2)) * 2
    if c > c2 and a[i] < c and a[i] <= min(a[max(r1, r2):i]):
        pen -= c - c2 - abs(a[i] - c2)
    pen2 = min(pen2, pen)

pen = abs(dr) + abs(c - c2)
print(min(pen + pen1, pen + pen2))
