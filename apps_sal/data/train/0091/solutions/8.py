t = int(input())
for tt in range(t):
    n = int(input())
    ent = list(map(int, input().split()))
    used = [0] * (n + 1)
    mnex = 1
    mx = 0
    ans = []
    ansex = True
    for i in range(n):
        if ent[i] > mx:
            mx = ent[i]
            if used[mx] == 0:
                ans.append(mx)
                used[mx] = 1
            else:
                ansex = False
                break
        else:
            while used[mnex] == 1:
                mnex += 1
            if mnex <= mx:
                used[mnex] = 1
                ans.append(mnex)
                mnex += 1
            else:
                ansex = False
                break
    if ansex:
        print(*ans)
    else:
        print(-1)
