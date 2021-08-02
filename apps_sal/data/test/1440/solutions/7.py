input()
cur = 0
res = 0
for a in map(int, input().split()):
    cur += a % 2
    a //= 2
    if a < cur:
        cur -= a
        res += a
    else:
        res += cur
        cur = (a - cur) * 2
        res += cur // 3
        cur %= 3
print(res)
