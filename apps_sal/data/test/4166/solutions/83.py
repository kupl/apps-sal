n, m = map(int, input().split())
 
s, c = [], []
for _ in range(m):
  s_, c_ = map(int, input().split())
  s.append(s_)
  c.append(c_)
 
for i in range(10**n):
  ans = str(i)
  if len(ans) == n and all([ans[s[j]-1] == str(c[j]) for j in range(m)]):
    print(ans)
    return
 
print(-1)
