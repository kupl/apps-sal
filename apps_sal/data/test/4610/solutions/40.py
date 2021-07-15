from collections import Counter
n,k = map(int, input().split())
a = list(map(int, input().split()))

cnt = Counter(a)

l = len(cnt)
t = l-k
ans = 0
for i in sorted(cnt.values()):
  if t <= 0: break
  t -= 1
  ans += i
print(ans)
