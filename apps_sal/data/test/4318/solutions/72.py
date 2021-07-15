N=int(input())
H=list(map(int, input().split()))

ans=1
Hbefore=H[0]

for i in range(1,N):
	if H[i]>=Hbefore:
		ans+=1
	
	Hbefore=max(Hbefore,H[i])

print(ans)
