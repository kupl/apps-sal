n = int(input())
s = list(map(int, input().split()))
ans = 0
for i in range(1, n):
  l = 0
  r = n-1
  cur = 0
  while True:
    l += i
    r -= i
    if l>=n or r<=i or (r%i==0 and r<=l):
      break
    cur += s[l] + s[r]
    ans = max(ans, cur)
print(ans)
