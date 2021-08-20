(n, k) = map(int, input().split())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
d = [[a[i], b[i], a[i] - b[i]] for i in range(n)]
del a, b
d = sorted(d, key=lambda x: x[2])
s = 0
for i in range(n):
    if k > 0:
        s += d[i][0]
        k -= 1
    else:
        s += min(d[i][0], d[i][1])
print(s)
