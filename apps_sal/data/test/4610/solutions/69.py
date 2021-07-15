from collections import Counter

n, K = map(int, input().split())
a = list(map(int, input().split()))
c = Counter()
for x in a:
  c[x] += 1

cv = [(k, x) for x, k in c.items()]
cv.sort(reverse=True)

ans = 0
while len(cv) > K:
  k,_ = cv.pop()
  ans += k
print(ans)
