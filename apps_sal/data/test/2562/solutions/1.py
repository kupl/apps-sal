n = int(input())
MAX = 1000005
mod = 1e9 + 7
po2 = [0]*(n+1)
po2[0] = 1
for v in range(1,n+1):
	po2[v] = (po2[v-1]*2)%mod
a = list(map(int,input().split()))
ta = [0]*MAX
for i in a:
	ta[i] += 1
cnt = [0]*MAX
for i in range(2,MAX):
	for j in range(i,MAX,i):
		cnt[i] += ta[j]
#print(ta[0:5],cnt[0:5])
ans = [0]*MAX
for i in range(MAX-1,0,-1):
	if cnt[i] == 0:
		continue
	ans[i] = (cnt[i]*po2[cnt[i]-1])%mod
	for j in range(i+i,MAX,i):
		ans[i] = (ans[i]+mod-ans[j])%mod
#print(ans[0:5])
endans = 0
for v in range(2,MAX):
	endans = (endans+v*ans[v])%mod
#print(po2)
print(int(endans))

