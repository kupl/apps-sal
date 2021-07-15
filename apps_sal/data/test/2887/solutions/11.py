n=int(input())
B=[int(i) for i in input().split()]
t=[int(i) for i in input().split()]
o=[]
for i in range(n):
     x=t[i]
     s=0
     for j in range(i+1):
          if(B[j]>x):
               B[j]=B[j]-x
               s+=x
          else:
               s+=B[j]
               B[j]=0
     o.append(s)
for i in o:
     print(i,end=" ")
               
          
          
          
     


