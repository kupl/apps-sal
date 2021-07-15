a=int(input())
#a1=a//2+1
d={}
#t=[]
dinv={}
for i in range(a):
	b1=input().split()
	b=list(b1)
	d[int(b[0])]=int(b[1]) #так мы создали словарик со всеми данными
#	t+=[int(b[1])]
	dinv[int(b[1])] = int(b[0])

c1=[]
n=0
#n=d.get(0)
#c1+=[n]
for i in range(a):
	n=d.get(n) # d[n]
	if n in d and n!=0:
		c1 += [n]
	#if n in d.values():
	#	c1+=[n] // создали первый список из всех четных студентов
	else:
		c1+=[n]
		break

#print(c1)
c2=[]
for i in d.keys():
	if i not in dinv:# and i!=0:
		k=i
		c2+=[k] #// нашли начало второго списка

for i in range(a):
	k=d.get(k)
	if k in d and k!=0:
		c2+=[k]  #// создали второй список (нечетные)
	else:
		c2+=[k]
		break
#print(c1)
#print(c2)
c1+=[0]
c2+=[0]
for i in range(a):
	if c2[i]!=0:
		print(c2[i], end=' ')
	if c1[i]!=0:
		print(c1[i], end=' ')
	else:
		break






