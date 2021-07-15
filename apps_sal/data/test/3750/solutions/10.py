k, a, b = map(int, input().split())

ca = a // k
cb = b // k

res = ca + cb

if a % k != 0:
    if cb == 0:
        res = -1

if b % k != 0:
    if ca == 0:
        res = -1

print(res)
