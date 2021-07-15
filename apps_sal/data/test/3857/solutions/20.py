N = int(input())
ar = list(map(int, input().split()))
ar.sort()

a = 1
b = 100
while a < b:
  compliant = True
  k = (a+b) // 2
  for i in range(len(ar)):
    if ar[i] < (i//k):
      compliant = False
      break
  if compliant:
    b = k
  else:
    a = k + 1
  
print(b)
