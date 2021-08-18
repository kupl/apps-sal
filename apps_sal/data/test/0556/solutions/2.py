
try:
    while True:
        l, r, k = list(map(int, input().split()))
        x = 1
        ls = []
        while x <= r:
            if x >= l:
                ls.append(x)
            x *= k
        if ls:
            print(' '.join(map(str, ls)))
        else:
            print(-1)

except EOFError:
    pass
