N,s=input().split()
n=int(N)

ans=0
for i in range(n):
    dic={'A':0,'T':0,'G':0,'C':0}
    for j in range(i,n):
        dic[s[j]]+=1
        if dic['A']==dic['T'] and dic['G']==dic['C']:
            ans+=1

print(ans)
