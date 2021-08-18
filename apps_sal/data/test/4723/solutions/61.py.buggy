S = input()
T = input()

if len(S) < len(T):
    print('UNRESTORABLE')
    return


ind = None
for i in range(len(S) - len(T) + 1):
    for j in range(len(T)):
        if S[i + j] == "?":
            continue
        elif S[i + j] == T[j]:
            continue
        else:
            break
    else:
        ind = i

if ind == None:
    print('UNRESTORABLE')
else:
    ans = list(S)
    for i in range(ind, ind + len(T)):
        ans[i] = T[i - ind]
    for i in range(len(ans)):
        if ans[i] == "?":
            ans[i] = "a"
    print("".join(ans))
