def tripleDoubles(N):
  last_sets = []
  for i in range(0, N):
    values = input().split(' ')
    last_sets.append(values)
    if len(last_sets) >= 3:
      doublesCounter = 0
      for item in last_sets[-3:]:
        if (item[0] == item[1]):
          doublesCounter += 1
      if doublesCounter == 3:
        return True
  return False

N = int(input())
print(('Yes' if tripleDoubles(N) else 'No'))

