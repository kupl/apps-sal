


dat = list(map(int, input().split()))
l = list(map(int, input().split()))


d = {}
i = 1
while i < dat[1] + 1:
  inter = list(map(int, input().split()))
  j = inter[0]
  while j < inter[1] + 1:
    if j not in d:
      d[j] = set()
    d[j].add(i)
    j+=1
  i+=1


max_res = -1 
ans = None

i = 0
while i  < len (l):
  j = 0
  while j < len (l):
    ii = i + 1
    jj = j + 1
    res_i = l[i]
    res_j = l[j]
    if ii in d:
      res_i = l[i] - len(d[ii])
      
      if jj in d:
        for dd in d[ii]:
          if dd in d[jj]:
            res_j -= 1

    res = res_j  - res_i
    if res > max_res:
      max_res = res
      ans = ii
    j += 1
  i += 1
  
if max_res == -1:
  print(0)
  print(0)
else:
  print(max_res)
  if ans in d:
    print(len(d[ans]))
    print(' '.join(map(str, d[ans])))
  else:
    print(0)


