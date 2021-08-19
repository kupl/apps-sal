import sys
sys.setrecursionlimit(10 ** 8)
n = int(input())
info = [list(map(int, input().split())) for i in range(n)]


def mex(array):
    if not array:
        return 0
    set_ = set(array)
    for i in range(10000):
        if i not in set_:
            return i


'\nres = 0\nfor a, k in info:\n    grundy = [0] * (a + 1)\n    for num in range(1, a + 1):\n        length = num // k\n        grundy[num] = mex(grundy[num - length:num])\n    res ^= grundy[-1]\n\nif res == 0:\n    print("Aoki")\nelse:\n    print("Takahashi")\n'
'\ndef solve(n, k):\n    if n % k == 0:\n        return n // k\n    return solve(n * (k - 1) // k, k)\n'


def solve(n, k):
    if n % k == 0:
        return n // k
    diff = n // k + 1
    target = n - n % k
    if (n - target) % diff == 0:
        return solve(target, k)
    n -= -(-(n - target) // diff) * diff
    return solve(n, k)


res = 0
for (a, k) in info:
    res ^= solve(a, k)
if res == 0:
    print('Aoki')
else:
    print('Takahashi')
