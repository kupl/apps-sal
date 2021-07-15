s = input()
l = [0]*2
for el in s:
    if el == 'L':
        l[0]+=1
    if el == 'R':
        l[0]-=1
    if el == 'U':
        l[1]+=1  
    if el == 'D':
        l[1]-=1       
l[0] = abs(l[0])
l[1] = abs(l[1])
if sum(l)%2!=0:
    print(-1)
else:
    print(sum(l)//2)
        

