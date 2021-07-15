s = int(input())
L = []
for c in range(2 , 10 ** 6 + 1):
  L.append(s)
  if s % 2 == 0:
    s = s // 2
  elif s % 2 == 1:
    s = s * 3 + 1
  if s in L:
    break
print(c)
