n = int(input())
a = sorted([int(i) for i in input().split()])
ans = 'YES'
for i in range(1, n):
  if a[i-1] == a[i]:
    ans = 'NO'
    break
print(ans)
