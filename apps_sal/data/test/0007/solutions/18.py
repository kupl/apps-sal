import sys
n, m = list(map(int, input().split()))
m = min(n - 1, m)
fday = -1
lday = n
while (fday + 1 < lday):
    mid = (fday + lday) // 2
    S = n - (mid * (mid + 1)) // 2 - m
    if (S <= 0):
        lday = mid
    else:
        fday = mid
print(min(n, m + lday))
