t = int(input())
n = 12
while t > 0:
    ans = []
    t = t - 1
    s = input()
    for i in range(n):
        r = i + 1
        if n % r != 0:
            continue
        c = n // r
        flag = False
        for j in range(c):
            id = j
            ff = False
            while id < n:
                if s[id] != 'X':
                    ff = True
                    break
                id = id + c
            if ff == False:
                flag = True
                break
        if flag == True:
            ans.append((r, c))
    print(len(ans), end='')
    for i in range(len(ans)):
        print(' ', ans[i][0], 'x', ans[i][1], sep='', end='')
    print('')
