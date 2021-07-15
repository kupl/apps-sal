S_ = input()
T = input()
len_T = len(T)
len_S = len(S_)

A = []
for i in range(len_S - len_T + 1):
    flg = True
    for t, s in zip(T, S_[i:i + len_T]):
        if s != '?' and s != t:
            flg = False
    if flg == True:
        S = ''
        for j in range(len_S):
            if i <= j < i + len_T:
                S += T[j - i]
            elif S_[j] == '?':
                S += 'a'
            else:
                S += S_[j]
        A.append(S)

ans = 'z' * (len_S + 1)
for S in A:
    if S < ans:
        ans = S
if ans == 'z' * (len_S + 1):
    print('UNRESTORABLE')
else:
    print(ans)
