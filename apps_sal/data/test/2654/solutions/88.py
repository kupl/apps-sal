n = int(input())
a = [0] * n
b = [0] * n
for i in range(n):
    a[i], b[i] = [int(j) for j in input().split()]
a.sort()
b.sort()
if n % 2 == 1:
    print(b[n//2] - a[n//2] + 1)
else:
    print(b[n//2] + b[n//2-1] - a[n//2] - a[n//2-1] + 1)
