from math import gcd

for _ in range(int(input())):
    m, d, w = list(map(int, input().split()))
    M = min(m, d)
    W = w // gcd(w, d - 1)
    Q = M // W
    R = M % W
    ans = (W - R) * (Q * (Q - 1) // 2) + R * (Q * (Q + 1) // 2)
    print(ans)
