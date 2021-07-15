N = int(input())
A = [0] + list(map(int, input().split()))

ans = 0
S = 0
X = 0
end = 0

for i in range(1, N+1):
  S -= A[i-1]
  X ^= A[i-1]
  if end == N:
    ans += end - i + 1
    continue
  if end < N:
    end += 1
  for j in range(end, N+1):
    S += A[j]
    X ^= A[j]
    if S != X:
      S -= A[j]
      X ^= A[j]
      end = j-1
      break
    if j == N:
      end = j
  ans += end - i + 1

print(ans)
