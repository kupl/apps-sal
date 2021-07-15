n = input()
n = n.split()
m = int(n[2])
k = int(n[1])
n = int(n[0])
a = input()
a = a.split()
b = int(a[0])
for c in range(n-2):
    b = b + int(a[c+1])
if b >= m * n:
    print(0)
elif b + k < m * n:
    print(-1)
else:
    print(m * n - b)
