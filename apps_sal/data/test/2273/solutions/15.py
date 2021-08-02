n, m = list(map(int, input().split()))
EE = []
if m < 3:
    print(-1)
else:
    edge = [set() for i in range(n)]
    a, b = list(map(int, input().split()))
    edge[a - 1].add(b - 1)
    edge[b - 1].add(a - 1)
    EE.append([a - 1, b - 1])

    for i in range(m - 1):
        x, y = list(map(int, input().split()))
        edge[x - 1].add(y - 1)
        edge[y - 1].add(x - 1)
        EE.append([x - 1, y - 1])
    c = 0
    for i in range(n):
        if a - 1 in edge[i] and b - 1 in edge[i]:
            c = i + 1
            break
    if c == 0:
        print(-1)
    else:
        Ans = [0] * n
        Ans[a - 1] = 1
        Ans[b - 1] = 2
        Ans[c - 1] = 3
        flg = True
        C = [1] * 3
        for i in range(n):
            if Ans[i] != 0:
                continue
            else:
                E = edge[i]
                if a - 1 in E and b - 1 in E and c - 1 not in E:
                    Ans[i] = 3
                    C[2] += 1
                elif a - 1 in E and b - 1 not in E and c - 1 in E:
                    Ans[i] = 2
                    C[1] += 1
                elif a - 1 not in E and b - 1 in E and c - 1 in E:
                    Ans[i] = 1
                    C[0] += 1
                else:
                    print(-1)
                    flg = False
                    break
        if flg:
            T = [0] * 3
            for x, y in EE:
                xx, yy = Ans[x], Ans[y]
                if xx == yy:
                    print(-1)
                    flg = False
                    break
                elif xx == 1 and yy == 2:
                    T[0] += 1
                elif xx == 2 and yy == 1:
                    T[0] += 1
                elif xx == 1 and yy == 3:
                    T[1] += 1
                elif xx == 3 and yy == 1:
                    T[1] += 1
                else:
                    T[2] += 1
        if flg:
            if T[0] == C[0] * C[1] and T[1] == C[0] * C[2] and T[2] == C[1] * C[2]:
                print(*Ans)
            else:
                print(-1)
