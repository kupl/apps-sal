import sys


def accept_input():
    S = input()
    T = input()
    return S, T


S, T = accept_input()
fromhere = -1
for i in range(len(S) - len(T) + 1):
    for j in range(len(T)):
        if S[i + j] == "?":
            continue
        elif S[i + j] == T[j]:
            continue
        elif S[i + j] != T[j]:
            break
    else:
        fromhere = i
if fromhere == -1:
    print("UNRESTORABLE")
    return
sd = ""
for i in range(len(S)):
    if i < fromhere:
        if S[i] == "?":
            sd += "a"
        else:
            sd += S[i]
    elif i >= fromhere + len(T):
        if S[i] == "?":
            sd += "a"
        else:
            sd += S[i]
    else:
        sd += T[i - fromhere]
print(sd)
