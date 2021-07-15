n, k = map(int, input().split())
count = 0
while n != 0:
  n = n//k
  count += 1
print(count)
