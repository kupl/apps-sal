input()
queue=list(map(int,input().split()))
t=len(queue)
base=min(queue)
minu=int(base/t)*t
while(queue[minu%t]>minu):
    minu+=1
print(minu%t+1) 
