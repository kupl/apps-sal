str1=input()
str2=input()
import sys
x=False
y=False
if(len(str1)!=len(str2)or len(str1)==1and str1[0]!=str2[0]):
    print("NO")
    return
else:
    for i in range(0,len(str1)):
      if(str1[i]=="1"):
          x=True
      if(str2[i]=="1"):
          y=True
if(len(str1)==1 and str1[0]=="0"and str2[0]=="0"):
    print("YES")
    return
if x==True and y==True or x==False and y==False:
    print("YES")
else:
    print("NO")

