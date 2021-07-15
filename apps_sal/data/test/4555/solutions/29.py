a, b, k = map(int, input().split())

if b-a <= k:
  for i in range(a, b+1):
    print(i)
else:
  ans = []
  for i in range(a, a+k):
    if i not in ans:
      ans.append(i)
      print(i)
  for j in range(b-k+1, b+1):
    if j not in ans:
      print(j)
