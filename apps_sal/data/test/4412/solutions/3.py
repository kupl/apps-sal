t = int(input())
for _ in range(t):
    n = int(input())
    ns = list(map(int, input().split()))
    ns.sort(reverse=True)
    from collections import OrderedDict
    ns = list(OrderedDict.fromkeys(ns))
    m = ns[0]
    ans = m
    if m % 30 == 0 and m // 2 in ns and (m // 3 in ns) and (m // 5 in ns):
        ans = m // 30 * 31
    c = m
    for i in range(len(ns)):
        if m % ns[i] != 0:
            c += ns[i]
            for j in range(i + 1, len(ns)):
                if m % ns[j] != 0 and ns[i] % ns[j] != 0:
                    c += ns[j]
                    break
            break
    ans = max(ans, c)
    print(ans)
