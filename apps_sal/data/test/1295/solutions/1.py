line1=input().split()
n=int(line1[0])
m=int(line1[1])
cities=input().split()
towers=input().split()
for i in range (n):
    cities[i]=int(cities[i])
for i in range (m):
    towers[i]=int(towers[i])

worst=0
i=0

for city in cities:
    if m>1:
        while (city>towers[i+1] and i+2<m):
            i+=1
        a=abs(towers[i]-city)
        b=abs(towers[i+1]-city)
        this=min(a,b)
        worst=max(worst,this)
    else:
        worst=max(worst,abs(towers[0]-city))
print (worst)

