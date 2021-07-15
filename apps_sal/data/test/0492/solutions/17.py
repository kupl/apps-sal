s=input()
n=int(input())
d={}
d['^']=0
d['>']=1
d['v']=2
d['<']=3

if n%4==2 or n%4==0:
	print("undefined")
else:
	sum=(d[s[2]]-d[s[0]]+4)%4;
	if(sum==n%4):
		print("cw")
	else:
		print("ccw")

