n = int(input())
a = list(map(int,input().split()))
tall = 0
ans = 0
for an in a:
  if an < tall:
    ans += tall - an
  elif an > tall:
    tall = an
print(ans)
