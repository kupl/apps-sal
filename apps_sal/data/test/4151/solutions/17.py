mod = 998244353

n = int(input())
a = list(map(int,input().split()))
d = {}

for i in range(n):
	d[a[i]] = i

i = 1
ans = 1
d2 = {}
ma = d[a[0]]
d2[a[0]] = 1

while i<n:
	tmp = d[a[i]]
	if a[i] in d2:
		i += 1
	elif i>ma:
		ans = (ans * 2)%mod
		d2[a[i]] = 1
	else:
		d2[a[i]] = 1
	ma = max(ma,tmp)

print(ans)
