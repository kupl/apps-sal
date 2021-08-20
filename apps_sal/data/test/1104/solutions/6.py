n = int(input())
flag = 0
argsa = list(map(int, input().split()))
argsb = list(map(int, input().split()))
argst = [0]
for i in range(n - 1):
    for j in range(4):
        if argst[i] & j == argsb[i] and argst[i] | j == argsa[i]:
            argst.append(j)
            flag = 1
            break
    if not flag:
        flag = 2
        break
    flag = 0
if flag == 2:
    flag = 0
    argst = []
    argst.append(1)
    for i in range(n - 1):
        for j in range(4):
            if argst[i] & j == argsb[i] and argst[i] | j == argsa[i]:
                argst.append(j)
                flag = 1
                break
        if not flag:
            flag = 2
            break
        flag = 0
if flag == 2:
    flag = 0
    argst = [2]
    for i in range(n - 1):
        for j in range(4):
            if argst[i] & j == argsb[i] and argst[i] | j == argsa[i]:
                argst.append(j)
                flag = 1
                break
        if not flag:
            flag = 2
            break
        flag = 0
if flag == 2:
    flag = 0
    argst = [3]
    for i in range(n - 1):
        for j in range(4):
            if argst[i] & j == argsb[i] and argst[i] | j == argsa[i]:
                argst.append(j)
                flag = 1
                break
        if not flag:
            flag = 2
            break
        flag = 0
if not flag == 2:
    print('YES', end='\n')
    print(*argst)
else:
    print('NO')
