import sys
n, m = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
a.sort()
b.sort()
for i in range(n):
    if a[i] in b:
        print(a[i])
        return
print(min(a[0], b[0])*10 + max(a[0], b[0]))
