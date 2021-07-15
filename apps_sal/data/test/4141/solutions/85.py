N = int(input())
An = list(map(int,input().split()))
ans = True
for i in An:
  if i % 2 == 0 and (i % 3 != 0 and i % 5 != 0):
    ans = False
if ans:
  print("APPROVED")
else:
  print("DENIED")
