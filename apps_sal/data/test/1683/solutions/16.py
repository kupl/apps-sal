n=int(input())
arr=list(map(str,input().split()))
cnt=[0]*12
for val in arr:
  cnt[len(val)]+=1
acumcnt=[0]*12
acumcnt[10]=cnt[10]
for i in range(9,-1,-1):
  acumcnt[i]=acumcnt[i+1]+cnt[i]
mod=998244353
ans=0
modarr=[0]*(20)
for i in range(20):
  modarr[i]=((10**i)%mod)%mod
for s in arr:
  for i in range(1,len(s)+1):
    tmp=int(s[-i])
    if i==1:
      ans+=((acumcnt[2]+cnt[1])*tmp*modarr[1])%mod
      ans+=((acumcnt[2]+cnt[1])*tmp*modarr[0])%mod
    elif i==2:
      ans+=((acumcnt[3]+cnt[2])*tmp*modarr[3])%mod
      ans+=((acumcnt[3]+cnt[2]+2*cnt[1])*tmp*modarr[2])%mod
    else:
      for j in range(i,i*2):
        if j==i*2-1:
          ans+=((acumcnt[i+1]+cnt[i])*tmp*modarr[j])%mod
        elif j==i*2-2:
          ans+=((acumcnt[i+1]+cnt[i]+2*cnt[i-1])*tmp*modarr[j])%mod
        else:
          ans+=(2*cnt[j-i+1]*tmp*modarr[j])%mod
print(ans%mod)
