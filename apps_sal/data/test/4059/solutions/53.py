n = int(input())
count = 0

for a in range(1, n + 1):
  for b in range(a, n + 1):
    if a * b >= n:
      break
    count += 2 if a != b else 1
     
print(count)
