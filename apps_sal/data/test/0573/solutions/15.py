n = int(input())
a = [int(i) for i in input().split()]
ones = a.count(1)
twos = a.count(2)
if ones <= twos:
  print(ones)
else:
  diff = ones - twos
  print(twos + diff//3)
