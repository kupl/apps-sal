n,k = map(int,input().split())
*l, = list(map(int,input().split()))
l.sort(reverse=True)
m = 0
ans = 0
for i in l:
  if m+i < k:
    m += i
    ans += 1
  else:
    ans = 0
print(ans)
