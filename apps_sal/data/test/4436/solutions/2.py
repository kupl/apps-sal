t = int(input())
for _ in range(t):
    n = int(input())
    test = 2
    out = []
    while len(out) < 2 and test * test < n:
        if n % test == 0:
            out.append(test)
            n //= test
        test += 1

    if len(out) == 2 and n > out[1]:
        print('YES')
        print(out[0], out[1], n)
    else:
        print('NO')
