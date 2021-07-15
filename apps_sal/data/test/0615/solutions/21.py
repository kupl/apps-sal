N = int(input())
A = list(map(int,input().split()))
B = [0]
tmp = 0
for a in A:
    tmp += a
    B.append(tmp)

l = 1
r = 3
cut = []
for i in range(2,N-1):
    Lm = float("inf")
    Rm = float("inf")
    c = [0,i,0]
    for j in range(l,i):
        tmp = abs(B[i]-2*B[j])
        if tmp > Lm:
            c[0] = j-1
            l = j-1
            break
        Lm = tmp
    else:
        c[0] = i-1
        l = i-1
    for k in range(r,N):
        tmp = abs((B[N]-B[k])-(B[k]-B[i]))
        if tmp > Rm:
            c[2] = k-1
            r = k-1
            break
        Rm = tmp
    else:
        c[2] = N-1
        r = N
    cut.append(c)
#print(cut)
ans = float("inf")
for p,q,r in cut:
    P = B[p]
    Q = B[q]-B[p]
    R = B[r]-B[q]
    S = B[N]-B[r]
    ans = min(ans,max(P,Q,R,S)-min(P,Q,R,S))
print(ans)

