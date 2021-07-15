n, k = map(int, input().split())
D = list(map(int, input().split()))

for i in range(n, 100000):
  m = str(i)
  count = 0
  for j in range(len(m)):
    if int(m[j]) in D:
      break
    else:
      count += 1
    if count == len(m):
      print(i)
      return
      
print(0)
