aa = int(input())
bb = int(input())
k1 = int(input())
k2 = int(input())
n = int(input())
if k1 >= k2:
    a = (aa, k1)
    b = (bb, k2)
else:
    a = (bb, k2)
    b = (aa, k1)
(a, k1) = (a[0], a[1])
(b, k2) = (b[0], b[1])
if (k1 - 1) * a + (k2 - 1) * b >= n:
    mini = 0
else:
    mini = min(a + b, n - (k1 - 1) * a - (k2 - 1) * b)
maxi = min(n // k2, b)
n = n - maxi * k2
maxi += min(a, n // k1)
print(mini, maxi)
