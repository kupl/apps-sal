a1 = int(input())
a2 = int(input())
k1 = int(input())
k2 = int(input())
n = int(input())
if k1 > k2:
    (a1, a2) = (a2, a1)
    (k1, k2) = (k2, k1)
lim = (k1 - 1) * a1 + (k2 - 1) * a2
mini = 0
maxi = 0
if n > lim:
    mini = n - lim
if n >= k1 * a1:
    n -= k1 * a1
    maxi += a1
else:
    rem = n // k1
    maxi += rem
    n -= rem * k1
rem = n // k2
maxi += rem
print(mini, maxi)
