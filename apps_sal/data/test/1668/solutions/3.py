def solve():
    n = int(input())
    d = {}
    ss = [input() for i in range(n)]
    for s in ss:
        d[s] = d.get(s,0)+1
    ans = sum(i-1 for i in d.values())
    print(ans)
    used = set(d.keys())
    l = []
    for s in ss:
        if d[s] > 1:
            t = list(s)
            f = False
            for i in range(4):
                for j in range(10):
                    t[i] = str(j)
                    u = "".join(t)
                    if u not in used:
                        l.append(u)
                        used.add(u)
                        d[s] -= 1
                        f = True
                        break
                if f:
                    break
        else:
            l.append(s)
            used.add(s)
    print(*l, sep="\n")

t = int(input())
for i in range(t):
    solve()
