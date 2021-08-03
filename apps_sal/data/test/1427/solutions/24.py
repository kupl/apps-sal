import math

mod = 10**9 + 7
N = int(input())
A = list(map(int, input().split()))
ans = 1
lcm = A[0]
for i in range(1, N):
    a = A[i]
    b = lcm
    gcd = math.gcd(a, b)
    lcm = (a * b) // gcd
    ans *= lcm // b
    ans += lcm // a
    ans %= mod

print(ans)
