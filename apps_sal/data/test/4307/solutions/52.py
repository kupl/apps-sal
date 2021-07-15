n = int(input())
count = 0
for i in range(1,n+1,2):
  ans = 0
  for j in range(1,n+1):
    if i % j == 0:
      ans += 1
  if ans == 8:
    count += 1
print(count)
