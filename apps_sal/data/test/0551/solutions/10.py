def test(id1,id2,l,n):
	a = l[id1] - l[id2]
	b = id2 - id1
	c = ((id1)*l[id2]) - ((id2)*l[id1])
	d=[]
	for i in range(n):
		if a*i+b*l[i]+c!=0:
			d+=[i]
	if len(d)==0:return False
	if len(d)==1:return True

	aa = l[d[0]] - l[d[1]]
	bb = d[1] - d[0]
	cc = ((d[0])*l[d[1]]) - ((d[1])*l[d[0]])

	for i in range(len(d)):
		if aa*d[i]+bb*l[d[i]]+cc!=0:
			return False
	return (l[id1]-l[id2])/(id1-id2)==(l[d[1]]-l[d[0]])/(d[1]-d[0]) 	
n=int(input())
l=[int(i)for i in input().split()]
print("Yes"if test(0,1,l,n) or test(1,2,l,n) or test(0,2,l,n) else "No" )
