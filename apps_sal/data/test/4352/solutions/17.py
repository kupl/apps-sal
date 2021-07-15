A, B = list(map(int, input().split()))

ans = ["Alice", "Bob", "Draw"]

if A == 1:
  A = 14
if B == 1:
  B = 14
  
if A > B:
  print((ans[0]))
elif A == B:
  print((ans[2]))
else:
  print((ans[1]))

