N = int(input())
A = list(map(int, input().split()))

ans = True
for i in A:
  if i%2 == 0 and not (i%3 == 0 or i%5 == 0):
    ans = False
    break
    
print("APPROVED" if ans else "DENIED")
