n, k = list(map(int, input().split()))
d = k*(k+1)//2
if n < d:
  print(-1)
else:
  u = 1
  for j in range(1, int(n**0.5)+2):
    if n % j == 0:
      jj = n // j 
      if j >= d and jj > u:
        u = jj
      elif jj >= d and j > u: 
        u = j
  res = [u*i for i in range(1, k)]
  res.append(n - sum(res))
  print(*res)
      
  

