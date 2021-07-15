import sys
sys.setrecursionlimit(10 ** 8)


n = int(input())
info = [list(map(int, input().split())) for i in range(n)]


# 愚直解
def mex(array):
    if not array:
        return 0
    set_ = set(array)
    for i in range(10000):
        if i not in set_:
            return i
"""
res = 0
for a, k in info:
    grundy = [0] * (a + 1)
    for num in range(1, a + 1):
        length = num // k
        grundy[num] = mex(grundy[num - length:num])
    res ^= grundy[-1]

if res == 0:
    print("Aoki")
else:
    print("Takahashi")
"""



# a(3n)=n, otherwise a(n)=a(floor(2n/3))
"""
def solve(n, k):
    if n % k == 0:
        return n // k
    return solve(n * (k - 1) // k, k)
"""

def solve(n, k):
    if n % k == 0:
        return n // k
    diff = (n // k) + 1
    target = n - n % k
    if (n - target) % diff == 0:
        return solve(target, k)
    n -= -((-(n - target)) // diff) * diff
    return solve(n, k)

res = 0
for a, k in info:
    res ^= solve(a, k)
if res == 0:
    print("Aoki")
else:
    print("Takahashi")
