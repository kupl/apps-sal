n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
d = []
def gsd(p, q):
    if q == 0:
        return p
    return gsd(q, p % q)
ans0 = 0
for i in range(n):
    if a[i] == 0:
        if b[i] == 0:
            ans0 += 1
        n -= 1
        i -= 1
        continue
    g = gsd(abs(a[i]), abs(b[i]))
    if a[i] * b[i] < 0:
        h = 1
    else:
        h = 0
    d.append([abs(b[i]) // g, abs(a[i]) // g, h])
d.sort()
bk = 0; k = 1
for i in range(1, n):
    if d[i] == d[i - 1]:
        k += 1
    else:
        bk = max(k, bk)
        k = 1
if n != 0:
    bk = max(bk, k)
print(bk + ans0)
#print(d)

