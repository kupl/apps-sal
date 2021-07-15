a,b=map(int,input().split())
total=a+b
s=0
e=1e10
while s!=e:
	g=(s+e+1)//2
	if g*(g+1)//2>total:
		e=g-1
	else:
		s=g
total_book=int(s)
books=[i for i in range(1,total_book+1)]
first_day=[]
sec_day=[]
k=len(books)
if a>=b:
	while k!=0 and a!=0:
		if a in books:
			first_day.append(a)
			c=a
			a-=books[c-1]
			del books[c-1]
		else:
			a-=books[-1]
			first_day.append(books[-1])
			del books[-1]
		k=len(books)
	sec_day=books[:]
else: 
	while k!=0 and b!=0:
		if b in books:
			sec_day.append(b)
			c=b
			b-=books[c-1]
			del books[c-1]
		else:
			b-=books[-1]
			sec_day.append(books[-1])
			del books[-1]
		k=len(books)
	first_day=books[:]
print(len(first_day))
for book in first_day:
	print(book,end=" ")
print()
print(len(sec_day))
for book in sec_day:
	print(book,end=" ")
print()
