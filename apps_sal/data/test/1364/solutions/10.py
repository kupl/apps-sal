n = int(input())
a = [int(i) for i in input().split(' ')]
p = a[0]
c = 1
b = []
for i in range(1, n):
    if a[i] != p:
        b.append(c)
        c = 1
        p = a[i]
    else:
        c += 1
b.append(c)
ma = -99
ans = 0
for i in range(0, len(b) - 1, 1):
    ma = max(min(b[i], b[i + 1]), ma)
print(2 * ma)
