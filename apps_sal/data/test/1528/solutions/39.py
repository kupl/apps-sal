(n, x) = list(map(int, input().split()))


def level_n_putty(n):
    if n == 0:
        return 1
    else:
        return 2 * level_n_putty(n - 1) + 1


def level_n_hb(n):
    if n == 0:
        return 1
    else:
        return 2 * level_n_hb(n - 1) + 3


m = level_n_hb(n)
s = 0
base = 0
while True:
    if x == base + 1:
        if n == 0:
            s += 1
        break
    elif x == base + m:
        s += level_n_putty(n)
        break
    else:
        l = level_n_hb(n - 1)
        if x < base + l + 2:
            base += 1
            n -= 1
            m = l
        elif x == base + l + 2:
            s += 1 + level_n_putty(n - 1)
            break
        else:
            base = base + l + 2
            s += 1 + level_n_putty(n - 1)
            n -= 1
            m = l
print(s)
