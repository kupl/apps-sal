n = int(input())
a = input().split()
a = [ int(i) for i in a ]
num = 0
maxa = a[0]
for i in range(1, len(a) ):
  if maxa < a[i]:
    maxa = a[i]
  elif maxa > a[i]:
    num += maxa - a[i]
  else:
    pass
print(num)
  
    
    


