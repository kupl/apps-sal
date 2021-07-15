n, k = map(int, input().split())
a = list(map(int, input().split()))
b = [0] * n
for i in range(n):
  if a[i] == 0:
    b[i] = min(k,i)

for i in range(n):
  if a[i] != 0:
    b[i] = b[a[i]-1] + min(2*k, i - a[i]) + 1
ans = [0] * n

for i in range(n):
  ans[i] = b[i] + min(k, n - i - 1) + 1

print(*ans)
