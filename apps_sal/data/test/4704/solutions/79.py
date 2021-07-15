N = int(input())
A = list(map(int, input().split()))

s = A[0]
a = sum(A[1:])

ans = abs(s - a)

for i in range(1, N-1):
  s += A[i]
  a -= A[i]
  ans = min(ans, abs(s - a))

print(ans)
