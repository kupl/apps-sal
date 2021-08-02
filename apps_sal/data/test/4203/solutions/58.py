S = str(input())

N = len(S)
flag = True
cnt = 0
if S[0] != 'A' or S[2:N - 1].count('C') != 1:
    flag = False
else:
    for i in range(N):
        if S[i].islower():
            cnt += 1
    if cnt != N - 2:
        flag = False
if flag:
    print('AC')
else:
    print('WA')
