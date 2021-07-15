A, B, C = map(int,input().split())
if A + B + C == 17  and max(A, B, C) == 7 and min(A, B, C) == 5:
  print("YES")
else:
  print("NO")
