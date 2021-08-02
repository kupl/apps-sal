def judge(Str, Len):
    if Str[:Len // 2] == Str[Len // 2:]:
        return True
    else:
        return False


S = input()
L = len(S)
i = 2 - (L % 2)
S = S[:-i]
L -= i
if judge(S, L):
    print(L)
else:
    while not judge(S, L):
        S = S[:-2]
        L -= 2
    print(L)
