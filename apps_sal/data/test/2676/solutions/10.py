n=int(input())
l=[]
for i in range(n):
 s=input()
 if s not in l:
  l.append(s)
m=int(input())
s=input()
c=0
for i in l:
 if i in s:
  c+=1
print(c) 
 

