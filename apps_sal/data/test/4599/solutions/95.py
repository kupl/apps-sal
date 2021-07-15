N = int(input())
a = list(map(int, input().split()))
a.sort(reverse = True)
ans = 0
for num in range(N):
  if num % 2 == 0:
    ans += a[num]
  else:
    ans -= a[num]
print(ans)
