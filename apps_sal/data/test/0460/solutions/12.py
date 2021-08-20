(p, x, y) = list(map(int, input().split()))
cur = x
while cur - 50 >= y:
    cur -= 50


def gen(s):
    i = s // 50 % 475
    res = []
    for _ in range(25):
        i = (i * 96 + 42) % 475
        res.append(26 + i)
    return res


while p not in gen(cur):
    cur += 50
print((max(cur - x, 0) + 99) // 100)
