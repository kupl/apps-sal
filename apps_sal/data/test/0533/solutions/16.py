a1 = int(input())
a2 = int(input())
k1 = int(input())
k2 = int(input())
n = int(input())
minn = 0
if n > (k1 - 1) * a1 + (k2 - 1) * a2:
    minn = n - ((k1 - 1) * a1 + (k2 - 1) * a2)
maxx = 0
if k1 > k2:
    (k1, k2) = (k2, k1)
    (a1, a2) = (a2, a1)
if k1 * a1 < n:
    maxx = a1 + min((n - k1 * a1) // k2, a2)
else:
    maxx = n // k1
print(minn, maxx)
