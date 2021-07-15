n = int(input())
k = int(input())
line = list(map(int, input().split()))
ans = 0
for i in range(n):
  ans += min(line[i], k-line[i]) * 2
print(ans)
