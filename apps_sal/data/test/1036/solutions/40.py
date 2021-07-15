N,k = map(int,input().split())
S = list(input())
def zyanken(a,b):
    if a == "R":
        if b == "P":
            return "P"
        else:
            return "R"
    elif a == "S":
        if b == "R":
            return "R"
        else:
            return "S"
    elif a == "P":
        if b == "S":
            return "S"
        else:
            return "P"
now = k
f = 0
if N == 1:
    print(S[0])
else:
    while now > 0:
        T = S + S
        for i in range(0,N):
            S[i]=(zyanken(str(T[(i*2)%N]),str(T[(2*i+1)%N])))
        now -= 1
    print(S[0])
