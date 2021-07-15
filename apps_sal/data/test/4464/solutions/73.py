A,B,C = list(map(int,input().split()))
R = C % B

found = False
for n in range(1,101):
  if n*A % B == R:
    found = True
    break
    
if found:
  print("YES")
else:
  print("NO")

