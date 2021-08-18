def dfs(x, d, g):
    g[x] = set()
    d[x] = 1

    if x % 2 == 0:
        next_ = x // 2

        if next_ not in d:
            g[x].add(next_)
            dfs(next_, d, g)
        elif next_ not in g[x]:
            g[x].add(next_)

    if x % 3 == 0:
        next_ = (x // 3) * 2

        if next_ not in d:
            g[x].add(next_)
            dfs(next_, d, g)
        elif next_ not in g[x]:
            g[x].add(next_)


def bfs(x, g):
    def add_prev(prev, cur_, next_):
        if next_ * 2 == cur_:
            prev[next_] = [cur_, 2]
        else:
            prev[next_] = [cur_, 3]

    min_ = {}
    s = [x]
    min_[x] = 0
    i = 0

    prev = {}

    while i < len(s):
        cur = s[i]
        for next_ in g[cur]:
            if next_ not in min_:
                min_[next_] = min_[cur] + 1
                s.append(next_)
                add_prev(prev, cur, next_)

            elif min_[cur] + 1 < min_[next_]:
                min_[next_] = min_[cur] + 1
                add_prev(prev, cur, next_)
        i += 1
    return min_, prev


def find(a1, b1, a2, b2, min1, prev1, min2, prev2):
    def process(a, b, type_):
        if type_ == 2:
            if a % 2 == 0:
                return a // 2, b
            else:
                return a, b // 2
        else:
            if a % 3 == 0:
                return (a // 3) * 2, b
            else:
                return a, (b // 3) * 2

    x1 = a1 * b1
    x2 = a2 * b2
    min_ = float('inf')
    num = None

    for x in min1:
        if x in min2:
            if min_ > min1[x] + min2[x]:
                min_ = min1[x] + min2[x]
                num = x

    if num == None:
        return -1, None, None

    cur1 = num
    arr1 = []
    while cur1 != x1:
        prev_, type_ = prev1[cur1]
        arr1.append(type_)
        cur1 = prev_

    cur2 = num
    arr2 = []
    while cur2 != x2:
        prev_, type_ = prev2[cur2]
        arr2.append(type_)
        cur2 = prev_

    for type_ in arr1[::-1]:
        a1, b1 = process(a1, b1, type_)

    for type_ in arr2[::-1]:
        a2, b2 = process(a2, b2, type_)

    return min_, [a1, b1], [a2, b2]


a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())

d1, g1, d2, g2 = {}, {}, {}, {}

dfs(a1 * b1, d1, g1)
dfs(a2 * b2, d2, g2)
min1, prev1 = bfs(a1 * b1, g1)
min2, prev2 = bfs(a2 * b2, g2)
ans, arr1, arr2 = find(a1, b1, a2, b2, min1, prev1, min2, prev2)

if ans == -1:
    print(-1)
else:
    print(ans)
    print(str(arr1[0]) + ' ' + str(arr1[1]))
    print(str(arr2[0]) + ' ' + str(arr2[1]))
