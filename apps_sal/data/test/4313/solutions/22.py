n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 0
for i in range(n):
  if a[i] - b[i] > 0:
    ans += a[i] - b[i]
print(ans)
