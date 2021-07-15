n=int(input())
a=[]
d={}
d['purple']='Power'
d['green']='Time'
d['blue']='Space'
d['orange']='Soul'
d['red']='Reality'
d['yellow']='Mind'
for i in range(n):
	a.append(input())
b=[]
print(6-n)
for i in d:
	if i not in a:
		print(d[i])

