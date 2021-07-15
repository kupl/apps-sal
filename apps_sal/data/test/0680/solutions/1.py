pos=[]
pos.append(list(map(int,input().split())))
pos.append(list(map(int,input().split())))
pos.append(list(map(int,input().split())))

pos.sort(key=lambda x:x[1])
#print(pos)
ans=[]
for i in range(min(pos[0][0],pos[1][0],pos[2][0]),max(pos[0][0],pos[1][0],pos[2][0])+1):
    ans.append([i,pos[1][1]])

if pos[0][1]<=pos[1][1]:
    for i in range(pos[0][1],pos[1][1]):
        ans.append([pos[0][0],i])
else:
    for i in range(pos[1][1]+1,pos[0][1]+1):
        ans.append([pos[0][0],i])


if pos[2][1]<=pos[1][1]:
    for i in range(pos[2][1],pos[1][1]):
        ans.append([pos[2][0],i])
else:
    for i in range(pos[1][1]+1,pos[2][1]+1):
        ans.append([pos[2][0],i])

print(len(ans))
for i in ans:
    print(i[0],i[1])
    


