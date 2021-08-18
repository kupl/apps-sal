def solve():
    def push(u, v, g):
        if u not in g:
            g[u] = []
        if v not in g:
            g[v] = []
        g[u].append(v)
        g[v].append(u)

    n = int(input())
    g = {}

    for _ in range(n - 1):
        u, v = map(int, input().split())
        push(u, v, g)

    for u in g:
        if len(g[u]) > 4:
            return 'NO', None
    d = {}
    build(1, 0, 0, 0, 31, -1, d, g)
    s = ''
    for u in range(1, n + 1):
        x, y = d[u]
        s += str(x) + ' ' + str(y)
        s += '\n'
    return 'YES', s


def cal_pos(dir_, cur_x, cur_y, cur_base):
    if dir_ == 0:
        return cur_x, cur_y + (1 << cur_base)
    elif dir_ == 1:
        return cur_x + (1 << cur_base), cur_y
    elif dir_ == 2:
        return cur_x, cur_y - (1 << cur_base)
    else:
        return cur_x - (1 << cur_base), cur_y


def build(u, p, cur_x, cur_y, cur_base, pre_dir, d, g):
    d[u] = [cur_x, cur_y]
    type_ = [0, 1, 2, 3]

    if pre_dir in type_:
        type_.remove(pre_dir)

    if u in g:
        for v in g[u]:
            if v != p:
                dir_ = type_.pop()

                next_x, next_y = cal_pos(dir_, cur_x, cur_y, cur_base)
                build(v, u, next_x, next_y, cur_base - 1, (dir_ - 2) % 4, d, g)


ans, s = solve()
if ans == 'NO':
    print(ans)
else:
    print(ans)
    print(s)
