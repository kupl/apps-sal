n,m = map(int, input().split())
a = [0] * m
b = [0] * m
for i in range(m):
    a[i], b[i] = map(int, input().split())
for i in range(n):
    print((a+b).count(i+1))
