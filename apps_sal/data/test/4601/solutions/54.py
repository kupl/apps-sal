h,k = list(map(int,input().split()))
lst = list(map(int,input().split()))
lst.sort()
if len(lst) >= k + 1:
  print((sum(lst[:len(lst)-k])))
else:
  print((0))


