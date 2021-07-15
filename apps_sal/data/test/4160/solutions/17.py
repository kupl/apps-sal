X = int(input())
i = 100
count = 0

while i < X:
  i += i//100
  count += 1

print(count)
