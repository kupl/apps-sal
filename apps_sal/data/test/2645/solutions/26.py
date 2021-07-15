s = str(input())
k = 0
p = 0
for i in range(len(s)):
  if k > 0:
    if s[i] == 'g':
      k -= 1
      p += 1
    else:
      k -= 1
  else:
    if s[i] == 'g':
      k += 1
    else:
      k += 1
      p -= 1
print(p)
      
    
     
  
  

