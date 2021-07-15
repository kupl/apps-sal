ord_a = ord('a')
L = 26

s = input()
k = int(input())

if len(s) < k:
  print('impossible')
  return

f = [False]*L

for c in s:
  f[ord(c)-ord_a] = True


print(max(k-sum(f),0))
