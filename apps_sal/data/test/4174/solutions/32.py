N, X  = map(int, input().split())
L = list(map(int, input().split()))
count = 1
distance = 0
for l in L:
  distance += l
  if distance <= X:
    count += 1
  else:
    break
print(count)
