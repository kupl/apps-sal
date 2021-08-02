q = int(input())
for i in range(q):
    n = int(input())
    ops = 0
    while not n % 2:
        n = n // 2
        ops += 1
    while not n % 3:
        n = n // 3
        ops += 2
    while not n % 5:
        n = n // 5
        ops += 3
    print(-1 if n > 1 else ops)
