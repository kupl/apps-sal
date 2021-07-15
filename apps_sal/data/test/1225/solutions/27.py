H = int(input())

i =0
temp = 0 
while True:
  if 2**(i)<=H and H<2**(i+1):
    temp = 2**(i)
    break
  i+=1
print (temp*2-1)
