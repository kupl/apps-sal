n = int(input())
l = list(map(int,input().split()))
l.sort()

ans = 0



if len(l) <= 2:
  print((0))
  return
  
for i in range(len(l)-2):
  for j in range(i+1,len(l)-1):
    for k in range(j+1,len(l)):
      if l[i] != l[j] and l[k] != l[j] and l[k] != l[i] and l[i] + l[j] > l[k]:
        ans += 1
       
        
print(ans)

