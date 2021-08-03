S = input()
ans = 'Yes'


def kaibun(Str):
    N = len(Str) // 2
    re = True
    for i in range(N):
        if Str[i] == Str[-i - 1]:
            continue
        else:
            re = False
    return re


N = len(S)
if not kaibun(S):
    ans = ('No')
if not kaibun(S[:(N - 1) // 2]):
    ans = ('No')
if not kaibun(S[(N + 3) // 2 - 1:]):
    ans = ('No')

print(ans)
