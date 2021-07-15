A, B, C, D = map(int,input().split())
m = A // D
n = C // B
if A % D != 0:
  m += 1
if C % B != 0:
  n += 1
if m >= n:
  print("Yes")
else:
  print("No")
