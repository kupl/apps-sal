n=int(input())
count=0
for i in range(n):
  A,B=map(int, input().split())
  if A==B:
    count+=1
    if count>=3:
      print("Yes")
      return
  else:
    count=0
print("No")      
