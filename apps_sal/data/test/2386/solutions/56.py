n = int(input())
As = list(map(int, input().split()))
for i in range(n):
  As[i] = As[i]-i
As = sorted(As)
b = As[n // 2]
ans = 0
for i in range(n):
  ans += abs(b - As[i])
print(ans)
