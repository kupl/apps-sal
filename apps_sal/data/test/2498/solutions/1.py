from functools import reduce
(N, M) = list(map(int, input().split()))
As = list(map(int, input().split()))
Bs = [A // 2 for A in As]


def gcd(a, b):
    while b:
        (a, b) = (b, a % b)
    return a


def lcm(a, b):
    return a // gcd(a, b) * b


nums = []
for B in Bs:
    num = 0
    while B % 2 == 0:
        B //= 2
        num += 1
    nums.append(num)
if len(set(nums)) != 1:
    ans = 0
else:
    L = reduce(lcm, Bs)
    ans = M // L - M // (2 * L)
print(ans)
