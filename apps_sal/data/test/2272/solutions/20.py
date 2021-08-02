def input_tuple(f):
    return tuple(map(f, input().rstrip().split()))


def make_edge(i1, i2, adj_list):
    i, a, b = i1
    j, c, d = i2
    if c < a < d or c < b < d:
        adj_list[i].append(j)


def dfs(curr, dest, seen, intervals):
    i, a, b = curr
    if i == dest:
        return True
    seen.add(i)
    for j, c, d in intervals:
        if j in seen:
            continue
        if c < a < d or c < b < d:
            if dfs((j, c, d), dest, seen, intervals):
                return True
    return False


def __starting_point():
    intervals = []
    num_queries = int(input().rstrip())
    i = 1
    for _ in range(num_queries):
        t, a, b = input_tuple(int)
        if t == 1:
            intervals.append((i, a, b))
            i += 1
        elif t == 2:
            if dfs(intervals[a - 1], b, set(), intervals):
                print('YES')
            else:
                print('NO')


__starting_point()
