from collections import defaultdict
N,s=input().split()
n=int(N)

ans=0
for i in range(n):
    dic=defaultdict(int)
    for j in range(i,n):
        dic[s[j]]+=1
        if dic['A']==dic['T'] and dic['G']==dic['C']:
            ans+=1

print(ans)
