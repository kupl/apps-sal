r, x,y,a,b = [int(x) for x in input().strip().split()]
dis = ((a-x)**2 + (b-y)**2)**0.5
ct = 0
while(dis>0):
	dis-= 2*r
	ct+=1
print(ct)

