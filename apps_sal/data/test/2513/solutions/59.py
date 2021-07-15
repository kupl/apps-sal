N = int(input())
S = input()

assignable = False

for k in range(4):
    res = [None for _ in range(N)]
    res[0] = k % 2
    res[-1] = k // 2
    for i in range(N - 2):
        if S[i] == 'o':
            if res[i] == 0:
                res[i + 1] = res[i - 1]
            else:
                res[i + 1] = 1 - res[i - 1]
        else:
            if res[i] == 0:
                res[i + 1] = 1 - res[i - 1]
            else:
                res[i + 1] = res[i - 1]
    if S[-2] == 'o':
        if res[-2] == 0:
            if res[-1] != res[-3]:
                continue
        else:
            if res[-1] != 1 - res[-3]:
                continue
    else:
        if res[-2] == 0:
            if res[-1] != 1 - res[-3]:
                continue
        else:
            if res[-1] != res[-3]:
                continue
    if S[-1] == 'o':
        if res[-1] == 0:
            if res[0] == res[-2]:
                assignable = True
        else:
            if res[0] == 1 - res[-2]:
                assignable = True
    else:
        if res[-1] == 0:
            if res[0] == 1 - res[-2]:
                assignable = True
        else:
            if res[0] == res[-2]:
                assignable = True
    if assignable:
        for i in range(N):
            if res[i]:
                print('W', end='')
            else:
                print('S', end='')
        break
else:
    print(-1)
