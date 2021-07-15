N = int(input())
A = list(map(int, input().split()))

other, two, four = (0, 0, 0)
for a in A:
  if a%4 == 0:
    four += 1
  elif a%2 == 0:
    two += 1
  else:
    other += 1
    
ans = "No"
if other <= four:
  ans = "Yes"
elif other-four == 1 and two == 0:
  ans = "Yes"
  
print(ans)

