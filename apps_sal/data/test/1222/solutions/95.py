from collections import deque
K = int(input())
queue = deque([1,2,3,4,5,6,7,8,9])
count = 1
while count <= K:
  num = queue.popleft()
  if num%10!=0:
    queue.append(num*10+num%10-1)
  queue.append(num*10+num%10)
  if num%10!=9:
    queue.append(num*10+num%10+1)
  count+=1
  
print(num)
