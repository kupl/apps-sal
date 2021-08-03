def read_data():
    n = int(input())
    xa = []
    for i in range(n):
        x, a = list(map(int, input().split()))
        xa.append((x, a))
    xa.sort()
    return n, xa


def solve(n, xa):
    count = 0
    for x, a in xa:
        if x < 0:
            count += 1
        else:
            break
    xa_minus = xa[:count]
    xa_plus = xa[count:]
    xa_minus.reverse()
    if len(xa_plus) > len(xa_minus):
        return sum(a for x, a in xa_plus[:len(xa_minus) + 1]) + sum(a for x, a in xa_minus)
    elif len(xa_plus) < len(xa_minus):
        return sum(a for x, a in xa_minus[:len(xa_plus) + 1]) + sum(a for x, a in xa_plus)
    else:
        return sum(a for x, a in xa)


n, xa = read_data()
print(solve(n, xa))
