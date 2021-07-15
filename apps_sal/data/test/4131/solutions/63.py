N,M = list(map(int,input().split()))
D = [[]for _ in range(N)]#元の入力順と設立年数を県ごとに保持するリスト

for i in range(M):
    p,y = list(map(int,input().split()))
    D[p-1].append((y,i))
ans = [0]*M
#print(D)

for i,d in enumerate(D):
    #print(i,d)
    d.sort()
    for k,(y,j)in enumerate(d):
        #print(k,(y,j))
        ans[j]=str(i+1).zfill(6)+str(k+1).zfill(6)

print(('\n'.join(ans)))



