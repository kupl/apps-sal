A, B, X = map(int, input().split())

def test(N):
  L = len(str(N))
  return A * N + B * L <= X

#二分探索
left = 0
right = 10 ** 30
while left + 1 < right:
  x = (left + right) // 2
  if test(x):
    left = x
  else:
    right = x
ans = left
if ans >= 10 ** 9:
  ans = 10 ** 9
print(ans)
