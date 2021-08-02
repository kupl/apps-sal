S = input()
N = len(S)
SS = S[0:(N - 1) // 2]
SSS = S[(N + 1) // 2:N + 1]

for i in range((N - 1) // 2):
    if S[i] != S[-1 - i]: print('No'); return
    if SS[i] != SS[-1 - i]: print('No'); return
    if SSS[i] != SSS[-1 - i]: print('No'); return
print('Yes')
