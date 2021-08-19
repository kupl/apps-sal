(a1, a2, k1, k2, n) = (int(input()) for i in range(5))
w1 = a1 * (k1 - 1)
w2 = a2 * (k2 - 1)
n1 = n - w1 - w2
mi = max(0, n1)
if k1 < k2:
    (k1, k2) = (k2, k1)
    (a1, a2) = (a2, a1)
l2 = n // k2
n2 = min(l2, a2)
n -= n2 * k2
l1 = n // k1
n3 = min(l1, a1)
print(mi, n3 + n2)
