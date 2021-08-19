import math

A, B, C, D = map(int, input().split())


def F(N):
    # N以下でどちらでも割れない
    x = N // C
    x += N // D
    lcm = C * D // math.gcd(C, D)
    x -= N // lcm
    return N - x


answer = F(B) - F(A - 1)
print(answer)
