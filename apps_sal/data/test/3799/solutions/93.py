# D問題
S = list(str(input()))
Slen = len(S)

fro = S[0]
bac = S[-1]

if fro == bac:
    if Slen % 2 == 0:
        print("First")
    else:
        print("Second")
else:
    if Slen % 2 == 0:
        print("Second")
    else:
        print("First")
