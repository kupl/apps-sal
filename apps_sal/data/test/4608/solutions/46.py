n = int(input())
a = []
for i in range(n):
  a.append(int(input()))
    
a.insert(0, 0)
ans = -1
push = 1

for i in range(1, n+2):
    
    if a[push] == 2:
        ans = i
        break
        
    else:
        push = a[push]
      
print(ans)
