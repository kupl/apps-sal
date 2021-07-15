def is_divide(an):
  for i, a in enumerate(an):
    if a % 2 == 0:
      an[i] = a / 2
    else:
      return False
  
  return True

n = int(input())
an = list(map(int, input().split()))

count = 0
while True:
  if not is_divide(an):
    break
  count += 1

print(count)

