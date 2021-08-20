def compress(ops):
    cops = []
    for (r, dir) in ops:
        while cops and cops[-1][0] <= r:
            cops.pop()
        if not cops or cops[-1][1] != dir:
            cops.append((r, dir))
    return cops


def transform(lst, ops):
    (mr, mdir) = ops[0]
    sections = [list(range(mr, len(lst)))]
    ost = 0
    oen = mr
    (pr, pdir) = ops[0]
    for (r, dir) in ops[1:]:
        k = pr - r
        if pdir:
            sections.append(reversed(list(range(ost, ost + k))))
            ost += k
        else:
            sections.append(list(range(oen - k, oen)))
            oen -= k
        (pr, pdir) = (r, dir)
    if pdir:
        sections.append(reversed(list(range(ost, oen))))
    else:
        sections.append(list(range(ost, oen)))
    olst = lst[:mr]
    olst.sort()
    olst.extend(lst[mr:])
    return [olst[i] for sec in reversed(sections) for i in sec]


def parse_op():
    (d, r) = input().split()
    return (int(r), d == '2')


def parse_input():
    (n, m) = list(map(int, input().split()))
    lst = list(map(int, input().split()))
    assert len(lst) == n
    ops = [parse_op() for _ in range(m)]
    return (lst, ops)


def __starting_point():
    (lst, ops) = parse_input()
    cops = compress(ops)
    tlst = transform(lst, cops)
    print(' '.join(map(str, tlst)))


__starting_point()
