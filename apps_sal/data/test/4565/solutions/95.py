N = int(input())
S = input()
a = S.count("E")
c = a 
 
for s in S:
  if s=="E":
    c-=1
  else:
    c+=1
  a=min(a,c)
 
print(a)
