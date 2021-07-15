import collections

t=int(input())
for _ in range(t):
  n=int(input())
  arr=list(map(int,input().split()))
  cnt=collections.Counter(arr)
  if n%2==1:
    print('Second')
  else:
    for val in cnt.values():
      if val%2==1:
        print('First')
        break
    else:
      print('Second')
