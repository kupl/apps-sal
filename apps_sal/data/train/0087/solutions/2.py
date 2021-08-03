import sys
import math

T = int(sys.stdin.readline().strip())
for t in range(0, T):
    m, d, w = list(map(int, sys.stdin.readline().strip().split()))
    w = w // math.gcd(w, d - 1)
    d = min(d, m)
    m = d
    ans = -d
    ans = ans + (m // w) * d
    m = m - (m // w) * w
    ans = ans + (d // w) * m
    d = d - (d // w) * w
    ans = ans + d
    print(ans // 2)
