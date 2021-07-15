H,A = map(int,input().split())

count = 0
while True:
  H = H-A
  count+=1
  if H<=0:
    break
  
print (count)
