n = int(input())
if n % 2 == 0:
    print(' '.join(map(str, [x for y in zip(range(2, n + 1, 2), range(1, n + 1, 2)) for x in y])))
else:
    print(-1)
