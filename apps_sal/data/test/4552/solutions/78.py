n = int(input())
f = [int(input().replace(" ", ""), 2) for i in range(n)]
p = [list(map(int, input().split())) for i in range(n)]
ans = -float('inf')
for i in range(1, 2 ** 10):
  sum = 0
  for j in range(n):
    sum += p[j][bin(i & f[j]).count('1')]
  ans = max(ans, sum)
print(ans)
