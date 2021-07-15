N, = map(int, input().split())
A = map(int, input().split())
for i in A:
  if i % 2 == 0 and not (i%3 == 0 or i%5==0):
    print("DENIED")
    return
print("APPROVED")    
