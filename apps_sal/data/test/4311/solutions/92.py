S = int(input())
array = []
array.append(S)

while True:
  count = 0
  if S % 2 == 0:
    S = S / 2
    array.append(S)
  else:
    S = 3 * S + 1
    array.append(S)
  for i in range(len(array)):
    if S == array[i]:
      count += 1
      if count == 2:
        print((i + 1))
        return

