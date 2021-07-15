n = int(input())
s = {}
for _ in range(n):
  t = "".join(sorted(input()))
  if t not in s: s[t] = 1
  else: s[t] += 1

ans = 0
for i in s.values(): ans += i*(i-1)//2
print(ans)
