n = int(input())
a = list(map(int, input().split()))

if n < 3:
  print(n)
  return

l, r = 0, 2
max_len = r - l
while r < n:
  while r < n and a[r] == a[r - 2] + a[r - 1]:
    r += 1
  max_len = max(max_len, r - l)
  l = r - 1
  r += 1

print(max_len)
