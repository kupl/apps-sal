def gene(l):
    d = {}
    for i in range(len(l)):
        if l[i] != i + 1:
            d[i + 1] = l[i]
    return d


def paired(d):
    return tuple(sorted(zip(list(d.keys()), list(d.values()))))


def exchange(d):
    if len(d) in (0, 2):
        yield paired(d)
    for i in d:
        if d[i] in d:
            if d[d[i]] == i:
                dp = {j: d[j] for j in d if j != i and j != d[i]}
                if len(dp) in (0, 2):
                    yield paired(dp)
            else:
                dp = {j: d[j] for j in d}
                dp[i], dp[d[i]] = dp[d[i]], dp[i]
                dp = {j: dp[j] for j in dp if j != dp[j]}
                if len(dp) in (0, 2):
                    yield paired(dp)
        else:
            assert(False)


n, m = list(map(int, input().split()))
ds = {((i, j), (j, i)) for i in range(1, m + 1) for j in range(i, m + 1)}
ds.add(tuple())
l = [ds for _ in range(n)]
for i in range(n):
    il = list(map(int, input().split()))
    if il == sorted(il):
        continue
    d = gene(il)
    # print(d)
    if len(d) > 4:
        print('NO')
        return
    l[i] = set(exchange(d))
    if not l[i]:
        print('NO')
        return
# print(l)

s = l[0]
for i in range(1, n):
    s = s.intersection(l[i])
# print(s)
if s:
    print('YES')
else:
    print('NO')
