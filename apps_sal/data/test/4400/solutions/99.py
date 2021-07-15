s = list(input())
count = 0
maximum = 0
while s:
  if s.pop() == 'R':
    count += 1
  else:
    maximum = max(maximum,count)
    count = 0
print(max(count,maximum))
