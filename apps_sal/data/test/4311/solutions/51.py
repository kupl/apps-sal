a = int(input())
 
x = set()
x.add(a)

i = 1
while True:
  i += 1
    
  if a % 2 == 0: a //= 2
  else: a = 3*a + 1
  
  if a in x: break
  x.add(a)
  
print(i)
