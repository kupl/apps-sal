n = int(input())
al = list(map(int,input().split()))
for i in al:
  if i%2 == 0:
    if i%3 != 0 and i%5 != 0:
      print("DENIED")
      return
      
print("APPROVED")
