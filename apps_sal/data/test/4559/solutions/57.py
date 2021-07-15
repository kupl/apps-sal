n = input()
a = list(map(int,input().split()))
ans = 1
a.sort()
for i in a:
  ans *= i
  if ans > 1000000000000000000:
    print(-1)
    return
print(ans)
