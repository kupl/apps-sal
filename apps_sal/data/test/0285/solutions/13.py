import sys


#sys.stdin = open("input.txt")
#sys.stdout = open("output.txt", "w")

n = int(input())

k = []
b = []
x1, x2 = (int(i) for i in input().split())

for i in range(n):
    k1, b1 = (int(j) for j in input().split())
    k.append(k1)
    b.append(b1)

zn = [(k[i] * x1 + b[i], k[i] * x2 + b[i]) for i in range(n)]
# print(zn)
zn.sort()
found = False
for i in range(n - 1):
    if zn[i][1] > zn[i + 1][1]:
        found = True
        break

if found:
    print("YES")
else:
    print("NO")
