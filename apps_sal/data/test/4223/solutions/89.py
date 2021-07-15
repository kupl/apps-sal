n = int(input())
bef = ""
ans = 0
for s in input():
  if bef != s:
    ans += 1
    bef = s
print(ans)
