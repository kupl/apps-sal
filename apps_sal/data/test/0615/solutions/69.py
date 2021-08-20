n = int(input())
a = list(map(int, input().split()))
b = [a[0]]
for i in range(1, n):
    b.append(b[-1] + a[i])
c = []
for i in range(n):
    c.append([abs(b[i] - b[-1] / 2), i])
h = -1
j = min(c, key=lambda x: x[0])[1]
p = 0
q = 0
r = b[j]
s = b[-1] - r
can = []
for i in range(n - 2):
    q += a[i]
    while True:
        pnew = p + a[h + 1]
        qnew = q - a[h + 1]
        if abs(pnew - qnew) < abs(p - q):
            h += 1
            p = pnew
            q = qnew
        else:
            break
    r -= a[i]
    while True:
        rnew = r + a[j + 1]
        snew = s - a[j + 1]
        if abs(rnew - snew) < abs(r - s):
            j += 1
            r = rnew
            s = snew
        else:
            break
    if 1 <= i < n - 2:
        can.append(max(p, q, r, s) - min(p, q, r, s))
print(min(can))
