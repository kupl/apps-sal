N = int(input())

if N == 1:
  print((0))
  return

if N % 2 == 0:
  a = N//2
  ans = (N-1)*a
else:
  a = (N-1)//2
  ans = (N)*a

print(ans)
    

