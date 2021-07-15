x = int(input())
ans = 0
while ans * (ans+1) / 2 < x:
  ans += 1
print(ans)
