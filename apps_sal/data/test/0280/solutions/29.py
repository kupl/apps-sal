import sys,itertools,bisect
input = sys.stdin.readline

N,M=list(map(int,input().split()))
W = [ int(w) for w in input().split()]
maxW = max(W)
lv=[list(map(int,input().split())) for _ in range(M)]
#橋の選別　ネックとなる橋の抽出　lj<=li,vj>=vi となる橋jはiに統合可能
lv.sort(key=lambda x:(x[1],-x[0]))
LV=[lv[0]]
for l,v in lv:
    if maxW>v:
        print((-1))
        return
    if LV[-1][0]<l:
        LV.append([l,v])
#LV.sort(key=lambda x:x[1])
V = [ v for _,v in LV]
L = [ l for l,_ in LV]
#らくだの順番でループ
ans = float('inf')

for perm in itertools.permutations(list(range(N)),N):
    dist = [0]*(N+1)#i番目までのラクダの必要距離 というか　座標
    #wgt = [0]*(N+1)#i-1番目までのラクダの重さの累積和
    #wgt[1] = W[perm[0]]
    for i in range(1,N):#iは終わりのインデックス　i含む
        #wgt[i+1]=wgt[i]+W[perm[i]]
        ww = W[perm[i]]
        for j in range(1,i+1):
            #toW = wgt[i+1]-wgt[j]
            ww +=W[perm[i-j]]
            idx = bisect.bisect_left(V,ww)-1
            if idx == -1:
                length = 0
            else:
                length = L[idx]
            dist[i+1]=max(dist[i+1],dist[i-j+1]+length)
    ans = min(ans,dist[-1])

print(ans)

