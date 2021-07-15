#E
N,P = list(map(int,input().split()))
S = list(str(input()))

zcount = S.count("0")

U = []
for i in range(N):
    u = int(S[N-i-1])
    U.append(u)
    
npow = 1
T = [0]
now = 0
for i in range(N):
    now += U[i]*npow
    now %= P
    T.append(now)
    npow*=10
    npow%=P
    
pmod = [0]*P
for t in T:
    pmod[t]+=1
    
ans1 = 0
for p in pmod:
    ans1 += (p*(p-1))//2
    
if P != 2 and P != 5:
    print(ans1)
else:
    ans2 = 0
    for i in range(N):
        u = U[i]
        if u%P == 0:
            ans2+=N-i
    print(ans2)


