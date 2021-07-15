n = int(input())
l = list(map(int, input().split()))

ans = 0
for k in l :
  ans = max(l.count(k), ans)
print(ans)

