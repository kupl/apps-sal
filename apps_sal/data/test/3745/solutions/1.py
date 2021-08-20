(n, m) = list(map(int, input().split()))
connectionList = []
for _ in range(n):
    connectionList.append([0] * n)
for _ in range(m):
    (p, q) = list(map(int, input().split()))
    connectionList[p - 1][q - 1] = 1
    connectionList[q - 1][p - 1] = 1
isDone = False
refList = []
ans = ['N'] * n
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if connectionList[i][j] == 0:
            isDone = True
            refList = (i, j)
            ans[i] = 'a'
            ans[j] = 'c'
            break
    if isDone:
        break
if not isDone:
    print('Yes')
    print('a' * n)
else:
    isPossible = True
    for i in range(n):
        if i in refList:
            continue
        elif connectionList[i][refList[0]] == 1 and connectionList[i][refList[1]] == 1:
            ans[i] = 'b'
        elif connectionList[i][refList[0]] == 0 and connectionList[i][refList[1]] == 1:
            ans[i] = 'c'
        elif connectionList[i][refList[0]] == 1 and connectionList[i][refList[1]] == 0:
            ans[i] = 'a'
        else:
            isPossible = False
            break
    if not isPossible:
        print('No')
    else:
        isValid = True
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if connectionList[i][j] == 0 and (ans[i] == 'a' and ans[j] == 'c' or (ans[j] == 'a' and ans[i] == 'c')):
                    pass
                elif not connectionList[i][j] == 0 and (not (ans[i] == 'a' and ans[j] == 'c' or (ans[j] == 'a' and ans[i] == 'c'))):
                    pass
                else:
                    isValid = False
        if isValid:
            print('Yes')
            print(''.join(ans))
        else:
            print('No')
