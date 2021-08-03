def mat(s, p):
    i = (s // 50) % 475
    for _ in range(25):
        i = (i * 96 + 42) % 475
        if i + 26 == p:
            return True
    return False


p, x, y = map(int, input().split())
s = x
while s >= y:
    s -= 50
if s < y:
    s += 50
while not mat(s, p):
    s += 50
if s <= x:
    print(0)
else:
    print(int((s - x) / 100 + 0.5))
