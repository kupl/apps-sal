M, K = map(int, input().split())

ans = [-1]
if M == 1:
  if K == 0:
    ans = [0, 0, 1, 1]
else:
  if K < 2**M:
    b = [i for i in range(2**M) if i != K]
    ans = b + [K] + b[::-1] + [K]

print(*ans)
