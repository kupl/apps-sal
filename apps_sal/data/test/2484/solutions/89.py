N = int(input())
A = list(map(int, input().split()))

ans = 0
S = 0
X = 0
end = -1

for i in range(N):
  while end < N-1:
    end += 1
    S += A[end]
    X ^= A[end]
    if S != X:
      S -= A[end]
      X ^= A[end]
      end -= 1
      break
  ans += end - i + 1
  S -= A[i]
  X ^= A[i]

print(ans)
