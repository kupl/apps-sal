a,ta=list(map(int,input().split(' ')))
#print (a,ta)
b,tb=list(map(int,input().split(' ')))

time=input()

hour=int(time[0:2])
mint=int(time[3:5])
low=(hour-5)*60+mint
up=low+ta
#print(low,up)
ans=0
for i in range(0,19*60,b):
	l=i
	h=i+tb
	if not (h <= low or l >= up):
		ans+=1
print (ans)
#print(hour)

