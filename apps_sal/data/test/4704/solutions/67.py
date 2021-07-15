n = int(input())
a = list(map(int, input().split()))

s = sum(a)

x = a[0]
ans = abs(x - (s - x))
for i in a[1:-1]:
  ans = min(ans, abs(x - (s - x)))
  x += i
print(ans)
