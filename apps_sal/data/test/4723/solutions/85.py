S = input()
T = input()
ans_list = []
for i in range(len(S) - len(T) + 1):
    X = S[i:i + len(T)]
    isOK = True
    for j in range(len(T)):
        if X[j] == '?' or X[j] == T[j]:
            pass
        else:
            isOK = False
            break
    if isOK:
        ans = S[:i] + T + S[i + len(T):]
        ans = ans.replace('?', 'a')
        ans_list.append(ans)
if len(ans_list) < 1:
    print('UNRESTORABLE')
else:
    ans_list.sort()
    print(ans_list[0])
