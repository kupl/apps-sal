t=int(input())
for i in range(t):
  dc = {}
  n=int(input())
  arr=[]
  out = 0
  hm = {}
  arr2 = []
  for i in range(n):
    tem=input()
    arr2.append(tem)
    if tem in dc:
      dc[tem]+=1
      out+=1
    else:
      dc[tem]=1
      arr.append(tem)
      hm[tem] = [tem]
  arr.sort()
  cur = 0
  for i in range(len(arr)):
    for j in range(dc[arr[i]]-1):
      cur = '0'
      trun = arr[i][:3]
      while trun+cur in dc:
        cur = chr(ord(cur)+1)
      dc[trun+cur] = 1
      hm[arr[i]].append(trun+cur)
  print(out)
  for i in range(len(arr2)):
    dc[arr2[i]] -= 1
    arr2[i] = hm[arr2[i]][dc[arr2[i]]]
    print(arr2[i])
