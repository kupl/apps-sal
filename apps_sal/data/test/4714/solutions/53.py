A, B = list(map(int, input().split()))

ans = 0

for i in range(A, B+1, 1):
  x = list(str(i))
  if x[0] == x[4] and x[1] == x[3]:
    ans += 1
else:
  print(ans)

