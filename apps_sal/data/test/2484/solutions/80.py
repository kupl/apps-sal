N = int(input())
A = list(map(int, input().split()))
ans = r = x = 0

for l in range(N):
  while r < l or r < N and x ^ A[r] == x + A[r]:
    x^=A[r]
    r+=1
  ans+=r-l
  x^=A[l]

print(ans)
