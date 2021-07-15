A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
i = j = k = l = m = 0
while i*10 < A:
  i = i+1
while j*10 < B:
  j = j+1
while k*10 < C:
  k += 1
while l*10 < D:
  l = l+1
while m*10 < E:
  m = m+1
a = (i+j+k+l+m)*10
s = [int(str(A)[-1]),int(str(B)[-1]),int(str(C)[-1]),int(str(D)[-1]),int(str(E)[-1])]
s_1 = [i for i in s if i != 0]
if s_1 == []:
  print(a)
else:
  num = min(s_1)
  print(a+num-10)
