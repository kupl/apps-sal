k = int(input())
li= list(map(int, input().split()))
li.sort()
sum=0
for k in range(len(li)):
  
  if k%2==0:
   
    sum=sum+li[k]
 
print(sum)

