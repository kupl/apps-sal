n = int(input())
m = int(input())
a = sorted([int(input()) for i in range(n)])
ans2 = max(a) + m
for i in range(n):
  m -= a[-1] - a[i]
  a[i] += a[-1] - a[i]
ans1 = a[-1] if m <= 0 else a[-1] + (m + n - 1) // n
print(ans1, ans2)

