import heapq
n=int(input())
array=input().split()
fin=[]
for i in array:
    fin.append(int(i))
if(len(fin)%2==0):
    fin.append(0)

heapq.heapify(fin)
sums=0
while(len(fin)>1):
    temp=0
    a=heapq.heappop(fin)
    b=heapq.heappop(fin)
    c=heapq.heappop(fin)
    temp=a+b+c
    sums+=temp
    heapq.heappush(fin,temp)
print(sums)
