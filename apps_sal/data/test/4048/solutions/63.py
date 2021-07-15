n  = int(input())
ans = n
cnt = 0
for i in range(2, int((n ** 0.5))+2):
  if n % i == 0:
    cnt += 1
    if ans > i + n/i -2:
      ans = i + n/i -2

if cnt == 0:
  ans = n-1
print(int(ans))
