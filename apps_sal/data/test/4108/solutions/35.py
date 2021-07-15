def p(S):
    D={}
    for i in range(len(S)):
        a=S[i]
        if a in D:
            D[a].add(i)
        else:
            D[a]={i}
    return D
S=input()
T=input()

A=sorted(p(S).values())
B=sorted(p(T).values())

if A==B:
    print("Yes")
else:
    print("No")

