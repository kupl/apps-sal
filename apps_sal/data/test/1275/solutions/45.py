n, k = list(map(int, input().split()))

# a+b = x, c+d = y, y=x-k
cnt = 0

for y in range(2, 2*n+1):
  if y <=n:
    q = y -1
  else:
    q = 2*n -y +1
  x = k+y
  if 2<= x <=2*n:
    if x <= n:
      p = x-1
    else:
      p = 2*n -x + 1
      
    cnt += p*q
print(cnt)

