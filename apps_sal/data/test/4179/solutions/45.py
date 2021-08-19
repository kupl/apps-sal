(n, m, c) = map(int, input().split())
b = list(map(int, input().split()))
e = 0
for i in range(n):
    a = list(map(int, input().split()))
    d = 0
    for i in range(len(b)):
        d = a[i] * b[i] + d
    if d + c > 0:
        e = e + 1
print(e)
