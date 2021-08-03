n = int(input())
a = []
b = []
a = input().split()
b = input().split()
for i in range(n):
    a[i] = int(a[i])
    b[i] = int(b[i])
b.sort()
if b[n - 1] + b[n - 2] >= sum(a):
    print('YES')
else:
    print('NO')
