t = input().split()[:3:]
s = set(t)
res = 3
if len(s)==1:
	res = min(res,0)
elif len(s)==2:
	res = min(res,1)
elif len(s)==3:
	res = min(res,2)
if res==0:
	print(res)
	return
t.sort()
m = [int(a[0]) for a in t if a[1]=='m']
p = [int(a[0]) for a in t if a[1]=='p']
s = [int(a[0]) for a in t if a[1]=='s']
def f(a):
	res = 2
	for i in a:
		if (i-1 in a and i+1 in a)or(i-2 in a and i-1 in a)or(i+1 in a and i+2 in a):
			return 0
		elif i-1 in a or i+1 in a or i-2 in a or i+2 in a:
			res = min(res,1)
	return res
res = min([res,f(m),f(p),f(s)])
print(res)
