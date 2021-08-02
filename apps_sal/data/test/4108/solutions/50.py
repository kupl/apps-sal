S = input()
T = input()
N = len(S)
# SからTの変換
d1 = {}
# TからSの変換
d2 = {}

for i in range(N):
    if S[i] not in d1:
        d1[S[i]] = T[i]
    else:
        if d1[S[i]] != T[i]:
            print("No")
            return
        else:
            pass

    if T[i] not in d2:
        d2[T[i]] = S[i]
    else:
        if d2[T[i]] != S[i]:
            print("No")
            return
        else:
            pass
print("Yes")
