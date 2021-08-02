Sp = str(input())
T = list(input())
ans = []
ANS = []
for i in range(len(Sp) - len(T) + 1):
    S = list(Sp)
    for j in range(len(T)):
        if S[i + j] == T[j] or S[i + j] == "?":
            S[i + j] = T[j]
            if j == len(T) - 1:
                ans.append(S)
        else:
            break
if len(ans) == 0:
    print('UNRESTORABLE')
else:
    for i in range(len(ans)):
        for j in range(len(Sp)):
            if ans[i][j] == "?":
                ans[i][j] = "a"
        ANS.append("".join(ans[i]))
    ANS.sort()
    print(ANS[0])
