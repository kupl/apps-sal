(n, m) = list(map(int, input().split()))


def get_connected_switches():
    lst = list(map(int, input().split()))
    lst.pop(0)
    return list([1 << d - 1 for d in lst])


cs = [get_connected_switches() for _ in range(m)]
ps = list(map(int, input().split()))
ans = 0
for on in range(2 ** n):
    ok = True
    for i in range(m):
        ct = 0
        for s in cs[i]:
            if s & on:
                ct += 1
        if ct % 2 != ps[i]:
            ok = False
    if ok:
        ans += 1
print(ans)
