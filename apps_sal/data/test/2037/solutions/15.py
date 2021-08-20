def main():
    buf = input()
    buflist = buf.split()
    n = int(buflist[0])
    m = int(buflist[1])
    buf = input()
    buflist = buf.split()
    a = list(map(int, buflist))
    answer = ''
    pool = {}
    table = set()
    for i in range(n):
        table.add(i + 1)
    for i in range(m):
        if a[i] in pool:
            pool[a[i]] += 1
        else:
            pool.update({a[i]: 1})
            table.remove(a[i])
        if len(table) == 0:
            answer += '1'
            for j in range(n):
                pool[j + 1] -= 1
                if pool[j + 1] <= 0:
                    pool.pop(j + 1)
                    table.add(j + 1)
        else:
            answer += '0'
    print(answer)


def __starting_point():
    main()


__starting_point()
