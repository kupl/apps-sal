n,k=list(map(int,input().split()))
s=str(input())
b=0
ip=[0 for i in range(256)]
for i in s:
   ip[ord(i)-97]+=1
for i in ip:
   if i>k:
      print("NO")
      b=1
      break
if b==0:
   print("YES")

