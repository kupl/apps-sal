(n, m) = list(map(int, input().split()))
a2 = set(range(1, n + 1))
a = list(map(int, input().split()))
a1 = set()
ans = ''
ns = {}
for i in a:
    a1.add(i)
    if i in ns:
        ns[i] = ns[i] + 1
    else:
        ns[i] = 1
    if a1 == a2:
        nns = {}
        for i in ns:
            ns[i] = ns[i] - 1
            if ns[i] != 0:
                nns[i] = ns[i]
        ns = nns
        a1 = set(ns)
        ans += '1'
    else:
        ans += '0'
print(ans)
