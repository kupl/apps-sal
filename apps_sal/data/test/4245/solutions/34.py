a, b = map(int, input().split())
c = 1
count = 0
while c < b:
  c += a - 1
  count += 1
print(count)
