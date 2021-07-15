n=int(input())
c=[int(x) for x in input().split()]
per={}
pos={}
i=1
for item in c:
    if item not in per:
        per[item]=i
    pos[item]=i
    i+=1
per1=[]
pos1=[]
for item in per:
    per1.append((per[item],item))
for item in pos:
    pos1.append((pos[item],item))
per1.sort()
pos1.sort(reverse=True)
if per1[0][1]!=pos1[0][1]:
    print(pos1[0][0]-per1[0][0])
else:
    print(max(pos1[0][0]-per1[1][0],pos1[1][0]-per1[0][0]))

