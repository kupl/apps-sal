n = int(input())
count = 0
for i in range(2, n+1):
  pre = i
  dic = {}
  while i % 2 == 0:
    if 2 not in dic:
      dic[2] = 2
    else:
      dic[2] += 1
    i //= 2
  f = 3
  while pow(f, 2) <= i:
    while i % f == 0:
      if f not in dic:
        dic[f] = 2
      else:
        dic[f] += 1
      i //= f
    f += 2
  if i != 1:
    dic[i] = 2
  num = 1
  for i in dic.values():
    num *= i
  if num == 8 and pre % 2 == 1:
    count += 1
print(count)
