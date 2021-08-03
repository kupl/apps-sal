T = int(input())
for t in range(T):
    N = int(input())
    Ans = [0] * N
    coll = []
    V = set()
    for n in range(N):
        s = input().strip()
        if s in V:
            coll.append((s, n))
        Ans[n] = s
        V.add(s)
    for c, pos in coll:
        for i in range(4):
            tVal = int(c[i])
            for j in range(1, 10):
                c = c[:i] + str((tVal + j) % 10) + c[i + 1:]
                if c not in V:
                    V.add(c)
                    break
            else:
                c = c[:i] + str(tVal) + c[i + 1:]
                continue
            break
        Ans[pos] = c
    print(len(coll), *Ans, sep='\n')
