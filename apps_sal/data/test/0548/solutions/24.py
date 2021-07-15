l=int(input())
seq=list(map(int, input().split()))
odd=0
even=0
tot=0
for i in seq:
  if i%2:
    odd+=1
    tot+=i
  else:
    even+=1
    tot+=i
if(tot%2):
  print("First")
else:
  if(odd):
    print("First")
  else:
    print("Second")
