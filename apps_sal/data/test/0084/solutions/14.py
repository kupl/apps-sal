import sys

lines = []
for line in sys.stdin:
    lines.append(line)

n = int(lines[0].rstrip("\r\n\t "))

max_price = n * 2 - 1
nines = len(str(max_price + 1)) - 1

if nines < 1:
    cnt = 0
    for x in range(1, n):
        cnt += x
    print(cnt)
    return

price_suffix = "9"*nines
cnt = 0


def add_pairs(max_x: int, p: int):
    nonlocal cnt
    from_max = int(p / 2)
    to_max = p - 1
    if to_max > max_x:
        to_max = max_x
    from_min = p - to_max
    cnt += from_max - from_min + 1


for d in range(0, 10):
    if d > 0:
        price = int(str(d) + price_suffix)
    else:
        price = int(price_suffix)
    if price <= max_price:
        add_pairs(n, price)

print(cnt)

