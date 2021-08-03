S = [int(d) for d in '{:04b}'.format(int(input()))]
S[0] = 1 - S[0]
if S[0]:
    S[1] = 1 - S[1]
if S[0] and S[1]:
    S[2] = 1 - S[2]
if S[0] and S[1] and S[2]:
    S[3] = 1 - S[3]
print(sum(2**(3 - i) * s for i, s in enumerate(S)))
