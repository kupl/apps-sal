S = input()
T = input()
anslist = []
for i in range(len(S) - len(T) + 1):
    kouho = [0] * len(S)
    ok = 1
    for j in range(len(T)):
        if S[i + j] == T[j] or S[i + j] == "?":
            kouho[i + j] = T[j]
        else:
            ok = 0
            break
    if ok == 1:
        for k in range(len(S)):
            if kouho[k] == 0:
                if S[k] != "?":
                    kouho[k] = S[k]
                else:
                    kouho[k] = "a"
        kouho = ''.join(kouho)
        anslist.append(kouho)
if len(anslist) == 0:
    ans = "UNRESTORABLE"
else:
    anslist.sort()
    ans = anslist[0]
print(ans)
