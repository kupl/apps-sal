import sys

def isKaibun(S):
    for i in range(len(S)//2):
        if not S[i] == S[len(S)-1-i]:
            return False
            return
    return True

S = input()
N = len(S)

S1 = S[0:(N-1)//2]
S2 = S[(N+3)//2-1:N]

if isKaibun(S) and isKaibun(S1) and isKaibun(S2):
    print("Yes")
else:
    print("No")
