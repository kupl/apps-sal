n, k = map(int, input().split())

lst = [ int(i) for i in input().split() ]
if len(lst) <= k:
  print(0)
  return
lst = sorted(lst)
for i in range(k):
  lst.pop()
print(sum(lst))
