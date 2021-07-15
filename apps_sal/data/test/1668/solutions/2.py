t = int(input())
for _ in range(t):
    n = int(input())
    a = []
    for i in range(n):
        a.append(input())

    added = set()
    everything = set(a)
    out = []
    res = 0
    for code in a:
        if code not in added:
            added.add(code)
            out.append(code)
        else:
            res += 1
            done = False
            for i in range(4):
                for d in range(9+1):
                    nw = code[:i] + str(d) + code[i+1:]
                    if nw not in everything:
                        added.add(nw)
                        everything.add(nw)
                        out.append(nw)
                        done = True
                        break
                if done: break
    print(res)
    print('\n'.join(out))

