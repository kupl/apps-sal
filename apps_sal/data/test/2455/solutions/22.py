t = int(input())
for _ in range(t):
    s = input()
    b = []
    for n in [1, 2, 3, 4, 6, 12]:
        m = 12 // n
        for j in range(m):
            if s[j::m] == 'X' * n:
                b += [(n, m)]
                break
    print(len(b), ' '.join((str(x) + 'x' + str(y) for (x, y) in b)))
