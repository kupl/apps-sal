import collections
url = 'https://atcoder.jp//contests/abc127/tasks/abc127_d'


def main2():
    (n, m) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    sumval = sum(a)
    a_counter = collections.Counter(a)
    bc = {}
    for _ in range(m):
        (b, c) = list(map(int, input().split()))
        bc.setdefault(c, 0)
        bc[c] += b
    a_tmp = sorted(list(a_counter.items()), key=lambda x: x[0])
    bc_tmp = sorted(list(bc.items()), key=lambda x: x[0], reverse=True)
    a_sort = [list(a_tmp[0])]
    bc_sort = [list(bc_tmp[0])]
    (count, aidx, bidx) = (0, 0, 0)
    while count <= m:
        if a_sort[aidx][0] >= bc_sort[bidx][0]:
            break
        tmp = min(a_sort[aidx][1], bc_sort[bidx][1])
        sumval = sumval - a_sort[aidx][0] * tmp + bc_sort[bidx][0] * tmp
        a_sort[aidx][1] -= tmp
        bc_sort[bidx][1] -= tmp
        if a_sort[aidx][1] == 0:
            aidx += 1
            if aidx >= len(a_tmp):
                break
            a_sort.append(list(a_tmp[aidx]))
        if bc_sort[bidx][1] == 0:
            bidx += 1
            if bidx >= len(bc_tmp):
                break
            bc_sort.append(list(bc_tmp[bidx]))
            count += 1
    print(sumval)


def __starting_point():
    main2()


__starting_point()
