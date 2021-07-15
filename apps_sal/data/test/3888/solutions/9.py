I=lambda:list(map(int,input().split()))
def med(a,b):
    if a==0 and b==0 or a==0 and b==2 or a==2 and b==0:
        return 1
    elif a==0 and b==1 or a==1 and b==0:
        return 2
    else:return 0
nagasa=4
N,=I()
A0=I()
AA=[A0]
Av=[A0[0]]+[int(input()) for _ in range(N-1)]
if N<=nagasa:
    for l in range(1,N):
        Ai=[Av[l]]
        for i in range(1,N):
            Ai.append(med(AA[l-1][i], Ai[-1]))
        AA+=[Ai]
    print(*(sum(al.count(i) for al in AA) for i in range(3)))
    return

for l in range(1,nagasa):
    Ai=[Av[l]]
    for i in range(1,N):
        Ai.append(med(AA[l-1][i], Ai[-1]))
    AA+=[Ai]
BB=[Av]
for c in range(1,nagasa):
    Bi=[A0[c]]
    for i in range(1,N):
        Bi.append(med(BB[c-1][i], Bi[-1]))
    BB+=[Bi]
*box,=(sum(al[:nagasa].count(i) for al in AA) for i in range(3))
*ass,=(sum(al.count(i) for al in AA) for i in range(3))
*bss,=(sum(bl.count(i) for bl in BB) for i in range(3))
less=[ass[i]+bss[i]-box[i] for i in range(3)]
less[AA[nagasa-1][nagasa-1]]+=N-nagasa
for i,a in enumerate(AA[nagasa-1]):
    if i<nagasa:continue
    less[a]+=N-1-i
for i,b in enumerate(BB[nagasa-1]):
    if i<nagasa:continue
    less[b]+=N-1-i
print(*less)
