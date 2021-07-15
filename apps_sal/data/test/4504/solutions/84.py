S=input()
S2=S[:(len(S))//2]
while len(S)>=2:
    S=S[:-2]
    S2=S2[:-1]
    if S==S2+S2:
        print((len(S)))
        return

