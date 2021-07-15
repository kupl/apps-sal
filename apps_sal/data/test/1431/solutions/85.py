N = int(input())
A = list(map(int, input().split()))
A.insert(0, 0)
ball = [0]*(N+1)
M = 0
ans = []
for i in reversed(range(1, N+1)):
  j = 2
  total = 0
  while i*j <= N:
    total += ball[i*j]
    j += 1
  if total%2 != A[i]:
    ball[i] = 1
    M += 1
for i in range(1, N+1):
  if ball[i] == 1:
    ans.append(i)
print(M)
print(*ans)
