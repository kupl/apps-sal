# 402B

from sys import stdin

__author__ = 'artyom'


def read_int_ary():
  return map(int, stdin.readline().strip().split())


n, k = read_int_ary()
a = list(read_int_ary())
mx = i_mx = 0
for i in range(n):
  if a[i] - k * i <= 0:
    continue
  sh = a[i] + k
  count = 0
  for j in range(i + 1, n):
    if a[j] == sh:
      count += 1
    sh += k
  if count > mx:
    mx = count
    i_mx = i

print(n - mx - 1)
sh = a[i_mx] - k * i_mx
for i in range(n):
  if a[i] < sh:
    print('+ ' + str(i + 1) + ' ' + str(sh - a[i]))
  elif a[i] > sh:
    print('- ' + str(i + 1) + ' ' + str(a[i] - sh))
  sh += k
