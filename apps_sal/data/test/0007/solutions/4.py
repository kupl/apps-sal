import sys
n, m = list(map(int, input().split()))


def check(i):
    se = ((m + i) * (i - m + 1)) // 2
    pr = m * (i -  m + 1)
    if (n >= (se - pr)):
        return True
    else:
        return False
if m >= n:
    print(n)
    return
m += 1
left = m
right = int(5e18) + 10
n -= m
while (right - left > 1):
    mid = (left + right) // 2
    if (check(mid)):
        left = mid
    else:
        right = mid
print(left)

