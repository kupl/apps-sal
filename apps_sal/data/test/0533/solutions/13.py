import sys
input = sys.stdin.readline
a1 = int(input())
a2 = int(input())
k1 = int(input())
k2 = int(input())
n = int(input())
if k1 <= k2:
    if k1 == k2:
        if a1 < a2:
            (a1, a2) = (a2, a1)
    maxx = min(n // k1, a1)
    n2 = n - maxx * k1
    maxx += min(n2 // k2, a2)
else:
    maxx = min(n // k2, a2)
    n2 = n - maxx * k2
    maxx += min(n2 // k1, a1)
minn = max(n - (k1 - 1) * a1 - (k2 - 1) * a2, 0)
print(minn, maxx)
