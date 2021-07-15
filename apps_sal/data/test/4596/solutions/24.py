N = int(input())
A = list(map(int, input().split()))

ans = 0

while True:
  exist_odd = False
  for n in range(N):
    if A[n] % 2 == 1:
      exist_odd = True
      break
    else:
      A[n] //= 2
  if exist_odd: break
  ans += 1

print(ans)

