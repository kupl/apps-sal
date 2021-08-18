n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ways = {(0, 0): [(0, 0)], (1, 0): [(0, 1), (1, 0)], (1, 1): [(1, 1)], (2, 0): [(2, 0), (0, 2)], (2, 2): [(2, 2)], (3, 0): [(3, 0), (0, 3), (2, 1), (1, 2)], (3, 1): [(3, 1), (1, 3)], (3, 2): [(3, 2), (2, 3)], (3, 3): [(3, 3)]}
ans = []
ddl = []
s = {0, 1, 2, 3}
for i in range(n - 2, -1, -1):
    if (a[i], b[i]) not in ways:
        print("NO")
        return
    d = ways[(a[i], b[i])]
    ns = set()
    dd = {None: None}
    for st, en in d:
        if (en in s):
            ns.add(st)
            dd[st] = en
    if i == 0:
        if len(ns) == 0:
            print("NO")
            return
        k = ns.pop()
        ans = [k, dd[k]]
    else:
        ddl.append(dd)
    s = ns

for i in range(1, n - 1):
    dd = ddl.pop()
    ans.append(dd[ans[-1]])


if ans[0] == None:
    print('NO')
else:
    print('YES')
    print(' '.join(map(str, ans)))
