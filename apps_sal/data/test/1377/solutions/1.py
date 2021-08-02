import sys

n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().strip().split()))
i = a.index(max(a))
v = True
for j in range(0, i):
    if a[j] > a[j + 1]:
        v = False
for j in range(i, n - 1):
    if a[j] < a[j + 1]:
        v = False
if v == True:
    print("YES")
else:
    print("NO")
