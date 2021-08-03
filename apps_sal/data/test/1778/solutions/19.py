from sys import stdin
n = int(stdin.readline())
a = [(int(x), 1) for x in stdin.readline().split()]
a.extend([(int(x), 2) for x in stdin.readline().split()])
a.sort(reverse=True)
asum = bsum = 0
al = 0
for i in range(n):
    if a[al][1] == 1:
        asum += a[al][0]
    al += 1
    if a[al][1] == 2:
        bsum += a[al][0]
    al += 1
print(asum - bsum)
