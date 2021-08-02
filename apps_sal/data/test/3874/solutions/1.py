n, m = list(map(int, input().split()))
w = [input() for _ in range(n)]
todel = [w[i - 1] for i in map(int, input().split())]
if len(set(map(len, todel))) != 1:
    print('No')
else:
    pat = ''.join(['?' if len(set([todel[j][p] for j in range(m)])) != 1 else todel[0][p] for p in range(len(todel[0]))])
    ok = True
    for x in w:
        if len(x) != len(pat):
            continue
        if not x in todel:
            mat = True
            for i in range(len(pat)):
                if pat[i] != '?' and pat[i] != x[i]:
                    mat = False
                    break
            if mat:
                ok = False
                break
    if not ok:
        print('No')
    else:
        print('Yes')
        print(pat)
