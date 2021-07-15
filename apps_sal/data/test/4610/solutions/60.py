from collections import Counter
N,K=map(int,input().split())
A=list(map(int,input().split()))

cnt=Counter(A)
cnt_sorted=sorted(cnt.items(), reverse=True,key=lambda x:x[1])

sum=0
for i in range(min(K,len(cnt))):
    sum+=cnt_sorted[i][1]

print(N-sum)
