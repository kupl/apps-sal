from math import ceil
n = int(input())


def solve(a, k):
    if a < k:
        return 0
    while a % k != 0:
        a -= ceil(a % k / (a // k + 1)) * (a // k + 1)
    return a // k


ans = 0
for _ in range(n):
    (a, k) = map(int, input().split())
    ans ^= solve(a, k)
if ans == 0:
    print('Aoki')
else:
    print('Takahashi')
