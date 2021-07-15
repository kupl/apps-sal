N,K=list(map(int,input().split()))
R,S,P=list(map(int,input().split()))
T=input()
cnt=[0 for _ in range(N)]
score={'r':P,'s':R,'p':S}
for i in range(N):
    if i<K:
        cnt[i]=score[T[i]]
    else:
        if T[i-K]!=T[i]:
            cnt[i]=score[T[i]]
        else:
            if cnt[i-K]==0:
                cnt[i]=score[T[i]]
print((sum(cnt)))

