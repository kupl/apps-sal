import itertools
# tempt
H,W,K=list(map(int,input().split()))
S=[input() for _ in range(H)]

ans=1e4 # 10000(10**4)
for t in itertools.product([0,1],repeat=H-1):
    cnt=t.count(1)
    SW=[]
    tmp=[int(s) for s in S[0] ]
    
    for i, c in enumerate(t):
        if c:
            SW.append(tmp)
            tmp = [int(s) for s in S[i + 1]]
        else:
            tmp = [tmp[j] + int(S[i + 1][j]) for j in range(W)]
    SW.append(tmp)
    H_ = len(SW)
    sums = [0] * H_
    if max(itertools.chain.from_iterable(SW)) > K:
        continue
    for w in range(W):
        sumtmp = [sums[i] + SW[i][w] for i in range(H_)]
        if max(sumtmp) > K:
            cnt += 1
            sums = [SW[i][w] for i in range(H_)]
        else:
            sums = sumtmp
    ans = min(ans, cnt)
print(ans)

