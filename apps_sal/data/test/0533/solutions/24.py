a1 = int(input())
a2 = int(input())
k1 = int(input())
k2 = int(input())
n = int(input())
n_min = a1 * (k1 - 1) + a2 * (k2 - 1)
ost = n - n_min
if ost <= 0:
    print(0, end=' ')
else:
    print(min(a1 + a2, ost), end=' ')
if k1 > k2:
    (k2, k1) = (k1, k2)
    (a1, a2) = (a2, a1)
d = n // k1
n_1 = min(a1, d)
n -= n_1 * k1
n_2 = min(a2, n // k2)
print(n_1 + n_2)
