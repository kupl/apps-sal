def mapt(fn, *args):
    return tuple(map(fn, *args))


def Input():
    return mapt(int, input().split(" "))


def main():
    n, m = Input()
    data = sorted([Input() for _ in range(n)])
    amount = 0
    for x, y in data:
        get1 = min(y, m)
        m = m - get1
        amount += get1 * x
        if m <= 0:
            return amount

print(main())
