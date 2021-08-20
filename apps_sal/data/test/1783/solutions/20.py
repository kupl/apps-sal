(n, k) = [int(x) for x in input().split()]
y = [0]
l = [int(x) for x in input().split()]
p = k
s = 0
for x in l:
    y.append(y[-1] + x)
ln = len(y)
while k < ln:
    s += y[k] - y[k - p]
    k = k + 1
print(s / (n - p + 1))
