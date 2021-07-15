from math import gcd

def lcm(a, b):
    return a // gcd(a, b) * b 

N, M = map(int, input().split())
As = list(map(int, input().split()))

rightmostbit = As[0] & -As[0]
for A in As[1:]:
    if rightmostbit != A & -A:
        print(0)
        return 


lcm_of_half_As = 1
for A in As:
    lcm_of_half_As = lcm(lcm_of_half_As, A //  2)
    if lcm_of_half_As > M:
        break

print((M // lcm_of_half_As + 1) // 2)
