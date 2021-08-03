import sys
input = sys.stdin.readline
# lev contains height from root,lower neighbour, higher neighbours
# lev[0] contains 0 (because it is the root), higher neighbours (=neighbours)
n = int(input())
p = list(map(int, input().split()))
p.insert(0, 0)
for i in range(1, n):
    p[i] -= 1
a = list(map(int, input().split()))
data = [0] * n
for i in range(n):
    data[i] = [0, a[i], True]
i = n - 1
biggest = 0
while i > 0:
    prev = p[i]
    if data[i][2]:
        data[i][0] += 1
    data[prev][0] += data[i][0]
    data[prev][1] += data[i][1]
    data[prev][2] = False
    biggest = max(biggest, 1 + (data[i][1] - 1) // data[i][0])
    i -= 1
biggest = max(biggest, 1 + (data[0][1] - 1) // data[0][0])
print(biggest)
