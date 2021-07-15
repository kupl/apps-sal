n = int(input())
max_count = 0
ans = 1
for i in range(1, n + 1):
  num = i
  count = 0
  while num % 2 == 0:
    num //= 2
    count += 1
  if count > max_count:
    ans = i
    max_count = count
print(ans)
