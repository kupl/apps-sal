n = int(input().strip())
ans=0
d = {'S':0,'M':0,'L':0,'XS':0,'XL':0,'XXS':0,'XXL':0,'XXXS':0,'XXXL':0,}
for i in range(n):
	d[input().strip()]+=1
d2 = {'S':0,'M':0,'L':0,'XS':0,'XL':0,'XXS':0,'XXL':0,'XXXS':0,'XXXL':0,}
for i in range(n):
	d2[input().strip()]+=1
for i in d2.keys():
	ans+=max(d2[i]-d[i],0)
print(ans)
