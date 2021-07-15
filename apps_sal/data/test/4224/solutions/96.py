n = int(input())
a = list(map(int,input().split()))
ans = 0
for v in a:
  cnt = 0
  while v%2==0:
    v //= 2
    cnt += 1
  ans += cnt
print(ans)
