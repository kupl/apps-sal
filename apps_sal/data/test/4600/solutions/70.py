(N, M) = map(int, input().split())
ACList = [0] * (N + 1)
ansAC = 0
ansP = 0
for i in range(M):
    (p, S) = map(str, input().split())
    p = int(p)
    if S == 'AC' and ACList[p] != -1:
        ansAC += 1
        ansP += ACList[p]
        ACList[p] = -1
    elif S == 'WA' and ACList[p] != -1:
        ACList[p] += 1
    else:
        continue
print(ansAC, ansP)
