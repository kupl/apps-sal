from collections import defaultdict
INF = 100_000_000
t = 1


for test in range(t):
    n = int(input())
    l = input()
    r = input()
    L = defaultdict(list)
    usedL = [False for i in range(n)]
    usedR = [False for i in range(n)]

    quesL = []
    quesR = []
    for i in range(n):
        if l[i] == "?":
            quesL.append(i)
            usedL[i] = True
        else:
            L[l[i]].append(i)

    ans = []
    for i in range(n):
        if r[i] == "?":
            quesR.append(i)
            usedR[i] = True
        else:
            if len(L[r[i]]) > 0:
                tmp = L[r[i]].pop()
                ans.append((tmp + 1, i + 1))
                usedL[tmp] = True
                usedR[i] = True

    usedL2 = []
    usedR2 = []
    for i in range(n):
        if not usedL[i]:
            usedL2.append(i)
        if not usedR[i]:
            usedR2.append(i)

    while len(quesL) > 0 and len(usedR2) > 0:
        ans.append((quesL.pop() + 1, usedR2.pop() + 1))

    while len(quesR) > 0 and len(usedL2) > 0:
        ans.append((usedL2.pop() + 1, quesR.pop() + 1))

    while len(quesL) > 0 and len(quesR) > 0:
        ans.append((quesL.pop() + 1, quesR.pop() + 1))

    print(len(ans))
    for i in ans:
        print(i[0], i[1])
