N = int(input())
ls = [int(i) for i in input().split()]
if len(ls) == 1:
  print(ls[0]*2)
else:
  als = [ls[0]]
  for n in range(1, N-1):
    als.append(min(ls[n-1], ls[n]))
  als.append(ls[-1])
  print(sum(als))
