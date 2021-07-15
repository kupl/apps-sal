n,m,k=list(map(int,input().split()))
wari=998244353


basum=0
for i in range(k+1):
	if i == 0:
		kumiawase=1
	else:
		kumiawase = kumiawase*(n-i)*pow(i,wari-2,wari)
		kumiawase %= wari
	basum += m * pow(m-1,n-i-1,wari) * kumiawase
	basum %= wari

print(basum)

