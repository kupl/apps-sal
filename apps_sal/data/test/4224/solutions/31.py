n = int(input())
lis = list(map(int, input().split()))
ans = 0

for i in range(n):
  con = 0
  if lis[i] % 2 == 0:
    x = lis[i]
    while x % 2 == 0:
      x = int(x / 2)
      con += 1
  ans += con   

print(ans)
