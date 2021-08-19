S = input()
rS = S[::-1]
le = len(S)
cent = int((le + 1) / 2)
S1 = S[0:cent - 1]
S2 = S[cent:]
rS1 = S1[::-1]
rS2 = S2[::-1]
if S == rS and S1 == rS1 and (S2 == rS2):
    print('Yes')
else:
    print('No')
