n = int(input())
a = list(map(int, input().split()))
d = 0
for i in range(n):
  d += 1 / a[i]
ans = 1 / d
print(ans)
