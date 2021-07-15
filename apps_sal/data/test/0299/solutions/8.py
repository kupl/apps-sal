c=input()
arr=[0,0,0]
inp=input()
inp=inp.split()
C=int(c)
v=0
for i in range(C):
    if v==3:
        v=0
        
    if v==0:
        arr[0]+=int(inp[i])
    elif v==1:
        arr[1]+=int(inp[i])
    elif v==2:
        arr[2]+=int(inp[i])

   

    v+=1

m=max(arr[0],max(arr[1],arr[2]))
if m==arr[0]:
    print ("chest")
elif m==arr[1]:
    print ("biceps")
else:
    print ("back")
    
    

