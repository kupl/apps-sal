n = int(input())
a = list(map(int,input().split()))
s=0
neg = -10000
pos = 10000
for i in range(n):
	if a[i]%2:
		if a[i]<0:
			neg = max(a[i],neg)
		else:
			pos = min(a[i],pos)
	if a[i]>0:s += a[i]
if neg%2 == 0: neg = 10000
if pos%2 == 0: pos = 10000
if s%2==0:
	s-=min(abs(neg),pos)
print(s)

