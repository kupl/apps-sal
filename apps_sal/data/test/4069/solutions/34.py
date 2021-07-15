import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(rs())
def rs_(): return [_ for _ in rs().split()]
def ri_(): return [int(_) for _ in rs().split()]

X, K, D = ri_()
x = abs(X)

if K * D <= x:
    ans = x - K * D
else:
    if K % 2 == 0:
        ans = min(x % (2 * D), abs(x % (2 * D) - 2 * D))
    else:
        ans = min(x % (2 * D) + D, abs(x % (2 * D) - D))
print(ans)
