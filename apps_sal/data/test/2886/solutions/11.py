S = input()
N = len(S)
S = "!" + S + "!"
if N == 2:
    if S[1] == S[2]:
        print("1 2")
    else:
        print("-1 -1")
    return
for i in range(1, N+1, 1):
    PrevAl = S[i-1]
    NowAl = S[i]
    NextAl = S[i+1]
    if PrevAl == NowAl or NowAl == NextAl or PrevAl == NextAl:
        AnsL = i-1
        AnsR = i+1
        if AnsL == 0:
            AnsL = 1
        print((AnsL, AnsR))
        return
print("-1 -1")

