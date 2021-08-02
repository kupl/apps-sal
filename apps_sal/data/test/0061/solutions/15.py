__author__ = 'cmashinho'

n, b = list(map(int, input().split()))
lB = list(map(int, input().split()))
m, y = list(map(int, input().split()))
lY = list(map(int, input().split()))

nB = 0
nY = 0

for i in range(n):
    nB += lB[i] * int(pow(b, (n - i - 1)))

for i in range(m):
    nY += lY[i] * int(pow(y, (m - i - 1)))

if nB == nY:
    print("=")
elif nB > nY:
    print(">")
else:
    print("<")
