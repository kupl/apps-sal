A, B, C = map(int, input().split())
s=set()

s.add(A)
s.add(B)
s.add(C)

if len(s)==2:
  print("Yes")
else:
  print("No")
