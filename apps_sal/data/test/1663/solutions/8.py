s=input()
ans=0
mod=10**9+7
n=len(s)
ps=[0]
cp=1
for i in range(n-1,-1,-1):
	ps.append((ps[-1]+int(s[i])*cp)%mod)
	cp=cp*10%mod
ps.reverse()
prefs=0
lastpref=0
for i in range(n):
	nextdigs=ps[i+1]
	ans=(ans+prefs*pow(10,n-i-1,mod)%mod+nextdigs*(i+1))%mod
	lastpref=(lastpref*10+int(s[i]))%mod
	prefs=(prefs+lastpref)%mod
print(ans)
