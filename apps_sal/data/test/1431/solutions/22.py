N = int(input())
a = list(map(int, input().split()))

b = [0] * N
for i in range(N):
  tmp = 0
  n = N-i
  for j in range(n*2-1, N, n):
    if b[j] == 1:
      tmp += 1
  if a[n-1] != tmp%2:
    b[n-1] = 1

ans = []
for i in range(N):
  if b[i] == 1:
    ans.append(i+1)
if ans != []:
  print(len(ans))
  print(*ans)
else:
  print(0)
