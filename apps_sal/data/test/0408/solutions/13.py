import sys
def R(): return list(map(int, input().split()))


n, m = R()
if 2 * n <= m:
    print(n)
elif 2 * m <= n:
    print(m)
else:
    print((m + n) // 3)
