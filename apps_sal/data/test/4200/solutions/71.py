n,m = map(int,input().split())
a = list(map(int,input().split()))
a.sort(reverse=True)
ans = 0
for i in a:
  if i >= sum(a)/(4*m):
    ans += 1
    if ans == m:
      print("Yes")
      return
  else:
    print("No")
    return
