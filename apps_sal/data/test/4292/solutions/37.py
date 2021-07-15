n, k = list(map(int, input().split()))
pArr = list(map(int, input().split()))

pArr.sort()
ans = 0
for i in range(k):
  ans += pArr[i]

print(ans)

