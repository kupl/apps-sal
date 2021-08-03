q = int(input())
for _ in range(q):
    n = int(input())
    wyn = 0
    pot = 1
    total = 1
    while total <= n:
        wyn += 1
        pot += 1
        total += (2**pot - 1) * (2**pot) // 2
    print(wyn)
