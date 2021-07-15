n, k = list(map(int, input().split()))
an = [int(num) for num in input().split()]

kind = {}
for a in an:
  if not a in kind:
    kind[a] = 1
  else :
    kind[a] += 1

sortedKind = sorted(list(kind.items()), key=lambda x:x[1])    

if len(sortedKind) > k:
  count = 0
  for check in sortedKind[:len(sortedKind)-k]:
    count += check[1]
  print(count)
else :
  print((0))

