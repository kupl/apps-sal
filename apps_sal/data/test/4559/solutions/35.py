n = input()
a = list(map(int,input().split()))
MX = 10**18
ans = 1
for i in a:
  if i == 0:
    print(0)
    return
for i in a:
    ans *= i
    if ans > MX:
      print(-1)
      return
print(ans)
