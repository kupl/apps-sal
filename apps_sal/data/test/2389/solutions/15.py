def select(x, y, ops, i, z):
    if not (x == 1 and y == 1 and (i < len(ops) - 1)):
        if x < y:
            return True
        else:
            return False
    op = ops[i]
    nop = ops[i + 1]
    oo = (op, nop)
    if op == nop:
        return True
    if oo in [('AB', 'AC'), ('BC', 'AB'), ('AC', 'AB')]:
        return True
    return False


def main():
    nabc = [int(_x) for _x in input().split()]
    n = nabc[0]
    a = nabc[1]
    b = nabc[2]
    c = nabc[3]
    ops = []
    for i in range(n):
        ops.append(input())
    result = []
    for i in range(n):
        op = ops[i]
        if op == 'AB':
            if select(a, b, ops, i, c):
                result.append('A')
                a += 1
                b -= 1
            else:
                result.append('B')
                a -= 1
                b += 1
        if op == 'AC':
            if select(a, c, ops, i, b):
                result.append('A')
                a += 1
                c -= 1
            else:
                result.append('C')
                a -= 1
                c += 1
        if op == 'BC':
            if select(b, c, ops, i, a):
                result.append('B')
                b += 1
                c -= 1
            else:
                result.append('C')
                b -= 1
                c += 1
        if a < 0 or b < 0 or c < 0:
            print('No')
            return
    print('Yes')
    for r in result:
        print(r)


main()
