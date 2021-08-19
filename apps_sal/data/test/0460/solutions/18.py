(p, x, y) = list(map(int, input().split()))


def f(s):
    rtn = []
    i = s // 50 % 475
    for _ in range(25):
        i = (i * 96 + 42) % 475
        rtn.append(26 + i)
    return rtn


ans = -1
tmp = x
while y <= tmp:
    if p in f(tmp):
        ans = 0
        break
    tmp -= 50
tmp = x
while ans < 0:
    tmp += 50
    if p in f(tmp):
        ans = (tmp - x + 50) // 100
print(ans)
