n = int(input())
a = [0] * n
b = [0] * n
for i in range(n):
    x, y = list(map(int, input().split()))
    a[i] = x + y
    b[i] = x - y
print((max(max(a) - min(a), max(b) - min(b))))
