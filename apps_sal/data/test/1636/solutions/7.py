def main():
    n = int(input())
    diag = [0] * 200005
    use = [0] * 200005
    for i in range(n):
        x, y = [int(i) for i in input().split(' ')]
        c = y - x
        if c > 0:
            diag[c] = max(x+1, diag[c])
        else:
            diag[c] = max(y+1, diag[c])

    table = set()
    for i in range(100005):
        table.add((-1, i))
        table.add((i, -1))

    result = []

    for v in [int(i) for i in input().split(' ')]:
        # print(v)
        if v > 0:
            x = use[v]
            y = x + v
        else:
            y = use[v]
            x = y - v

        # print(x, y, use[v], diag[v], use[v] > diag[v], (x-1, y) not in table, (x, y-1) not in table)

        use[v] += 1

        if use[v] > diag[v]:
            print ('NO')
            return

        if (x-1, y) not in table or (x, y-1) not in table:
            print ('NO')
            return
        table.add((x, y))
        result.append((x, y))

    print('YES')
    for v in result:
        print(v[0], v[1])

main()
