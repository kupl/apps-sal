from operator import itemgetter

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(m)]

b = sorted(a, key=itemgetter(1))
#print(b)
removed = -1
ans = 0

for i in range(m):
  if b[i][0] > removed:
    removed = b[i][1] - 1
    ans += 1
    
print(ans)
