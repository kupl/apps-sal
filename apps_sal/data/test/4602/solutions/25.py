n = int(input())
k = int(input())
x = [int(x.strip()) for x in input().split()]
ans = 0
for i in x:
  if abs(i-k) > i:
    ans = ans + i
  else:
    ans = ans + abs(i-k)
ans += ans
print(ans)
