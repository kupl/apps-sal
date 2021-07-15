N = int(input())
L = list(map(int, input().split()))

count = 0
for i in range(N-2):
  a = L[i]
  for j in range(N-2-i):
    b = L[i+j+1]
    if a == b:
      continue
    for k in range(N-2-i-j):
      c = L[i+j+k+2]
      if a == c or b == c:
        continue
      if a+b>c and b+c>a and c+a>b:
        count+=1

print(count)
