A,B,C,D = map(int,input().split())
if A>D or B<C:
  print(0)
  return
if C>A:
  A = C
if D<B:
  B = D
print(B-A)
