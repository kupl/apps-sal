S = input()
T = input()
len_S, len_T = len(S), len(T)
ans = []
for i in range(len_S - len_T + 1):
    f = True
    for j in range(len_T):
        if S[i + j] != T[j] and S[i + j] != '?':
            f = False
            break
    if f:
        s = S[:i] + T + S[i + j + 1:]
        ans.append(s.replace('?', 'a'))
if len(ans) == 0:
    print('UNRESTORABLE')
else:
    ans.sort()
    print(ans[0])
