n,m=map(int,input().split())
arr=list(map(int,input().split()))
d={}
res = ""
for i in arr:
	if i in d:
		d[i]+=1
	else:
		d[i]=1
	is_round = (len(d) == n)
	res+=str(int(is_round))
	if is_round:
		d2= {}
		for k, v in d.items():
			if v > 1:
				d2[k] = v - 1 
		d = d2

print(res)
