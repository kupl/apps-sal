N,K=map(int,input().split())
R,S,P=map(int,input().split())
T=input()

moi=[['x'] for i in range(K)]

for i in range(N):
    moi[i%K].append(T[i])

for i in range(K):
    moi[i].pop(0)

moji=''

for i in range(K):
    cnt=0
    for j in range(len(moi[i])):
        if j==0:
            moji+=moi[i][j]
        else:
            if moi[i][j-1]!=moi[i][j]:
                moji+=moi[i][j]
                cnt=0
            if moi[i][j-1]==moi[i][j] and cnt==1:
                moji+=moi[i][j]
                cnt=0
            elif moi[i][j-1]==moi[i][j] and cnt==0:
                cnt+=1

ans=0
for i in range(len(moji)):
    if moji[i]=='r':
        ans+=P
    elif moji[i]=='s':
        ans+=R
    else:
        ans+=S

print(ans)
