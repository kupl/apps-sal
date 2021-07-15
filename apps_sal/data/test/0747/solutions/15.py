import queue
n,maxh=[int(x) for x in input().split()]
car=[]
fru=[]
hcar=queue.PriorityQueue(2000)
hfru=queue.PriorityQueue(2000)
for i in range(n):
	a,b,c=[int(x) for x in input().split()]
	if a==0:
		car.append((b,c))
	else:
		fru.append((b,c))
pcar=0
mcar=len(car)
pfru=0
mfru=len(fru)
car.sort()
fru.sort()
eaten=0
def getinh():
	nonlocal pcar
	nonlocal pfru
	while pcar<mcar and car[pcar][0]<=maxh:
		hcar.put(-car[pcar][1])
		pcar+=1
	while pfru<mfru and fru[pfru][0]<=maxh:
		hfru.put(-fru[pfru][1])
		pfru+=1
getinh()
while (not hcar.empty()) and (not hfru.empty()):
	eaten+=2
	maxh-=hcar.get()+hfru.get()
	getinh()
if hcar.empty():
	now=0
else:
	now=1

while True:
	if now==0:
		if hfru.empty():
			break
		else:
			now=1
			maxh-=hfru.get()
	else:
		if hcar.empty():
			break
		else:
			now=0
			maxh-=hcar.get()
	eaten+=1
	getinh()
print(eaten)

