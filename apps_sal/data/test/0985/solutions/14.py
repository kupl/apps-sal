n = int(input())
B = 1000
d = [0] * 2222
D = [0] * 2222
for i in range(n):
    x, y = list(map(int, input().split()))
    d[x - y + B] += 1
    D[x + y] += 1
s = 0
for e in d:
    if e >= 2:
        s += e * (e - 1)
for e in D:
    if e >= 2:
        s += e * (e - 1)
s >>= 1
print(s)
