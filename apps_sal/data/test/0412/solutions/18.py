n = int(input())
a = [int(i) for i in input().split()]
b = 0
c = 0
d = []
for i in range(n):
    while True:
        b = a[i] / 2 ** c
        if b != int(b):
            break
        c += 1
    d.append(2 ** (c - 1))
    c = 0
p = max(d)
p1 = d.count(p)
print(p, p1)
