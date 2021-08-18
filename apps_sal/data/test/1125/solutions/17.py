from functools import lru_cache

N = int(input())
A = list(map(int, input().split()))

tmp = 0
for a in A[2:]:
    tmp ^= a

INF = 10 ** 18


@lru_cache(None)
def F(a, b, xor):
    if (a & 1) ^ (b & 1) != (xor & 1):
        return INF
    if xor == 0:
        return INF if a < b else (a - b) // 2
    x = 2 * F(a // 2, b // 2, xor // 2)
    y = 2 * F((a - 1) // 2, (b + 1) // 2, xor // 2) + 1

    x = min(x, y)
    if x >= INF:
        x = INF

    return x


x = F(A[0], A[1], tmp)
if x >= A[0]:
    x = -1

print(x)
