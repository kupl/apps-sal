import collections

S=list(str(input()))
num=collections.Counter(S)

for i,j in num.items():
   if j!=2:
       print("No")
       return
       
print("Yes")
