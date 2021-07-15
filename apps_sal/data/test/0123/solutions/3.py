import sys
n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
need = a.count(0)
b.sort(reverse = True)
ptr = 0
for i in range(n):
    if (a[i] == 0):
        a[i] = b[ptr]
        ptr += 1
z = a[:]
z.sort()
if (z == a):
    print('No')
else:
    print('Yes')

