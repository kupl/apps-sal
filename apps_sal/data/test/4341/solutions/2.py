T = input().split(' ')
n = int(T[0])
m = int(T[1])
B = [0] * (n+1)
S1 = [0] * (n+1)
S2 = [0] * (n+1)
for i in range(m):
    S = input().split(' ')
    a = int(S[0])
    b = int(S[1])
    if S1[a]==0:
        S1[a] = b
    elif S2[a]==0:
        S2[a] = b
    else:
        B[a] = 1
        B[b] = 1
    if S1[b]==0:
        S1[b] = a
    elif S2[b]==0:
        S2[b] = a
    else:
        B[a] = 1
        B[b] = 1
for i in range(1, n+1):
    if S1[i] == 0 or S2[i] == 0:
        B[i] = 1
sol = 0
for ind in range(1, n+1):
    if B[ind] == 0:
        v = ind
        w = S2[ind]
        c = True
        while w!=ind:
            B[v] = 1
            if B[w] == 0:
                u = w
                if S1[w]==v:
                    w = S2[w]
                else:
                    w = S1[w]
            else:
                B[ind] = 0
                c = False
                break
            v = u
        if c:
            B[v] = 1
            sol+=1
print(sol)
        

