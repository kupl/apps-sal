n = int(input())
day = 1

for i in range(n):
  start, extra = list(map(int, input().split()))
  day = max(day, start)

  while (day - start) % extra != 0:
    day += 1
  if i + 1 < n:
    day += 1

print(day)

