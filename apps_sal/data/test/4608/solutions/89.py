n = int(input())
btn = {b+1: int(input()) for b in range(n)}
cur = 1
cnt = 0
while cnt <= n and cur != 2:
  cur = btn[cur]
  cnt += 1
  if cur == 2:
    print(cnt)
    return
print(-1)
