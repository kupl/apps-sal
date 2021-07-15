# cook your dish here
n=int(input())
s=[int(j) for j in input().split()]
t=[int(j) for j in input().split()]
l=[]
for i in range(n):
  te=t[i]
  l.append(s[i])
  l1=[]
  ans=0
  for i in l:
      if(i>te):
          ans+=te
          l1.append(i-te)
      else:
          ans+=i
  l=l1
  print(ans,end=" ")  
