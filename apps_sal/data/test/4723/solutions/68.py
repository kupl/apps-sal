S = str(input())
T = str(input())
ls = len(S)
lt = len(T)

ans = ''
loc = None
for i in range(ls - lt, -1, -1):
    flag = 0
    for j in range(lt):
        if not (S[i + j] == T[j] or S[i + j] == '?'):
            flag = 1
            break
    if flag == 0:
        loc = i
        break

if loc == None:
    print('UNRESTORABLE')
else:
    i = 0
    while i < ls:
        if i == loc:
            ans += T
            i += lt
        elif S[i] == '?':
            ans += 'a'
            i += 1
        else:
            ans += S[i]
            i += 1
    print(ans)
