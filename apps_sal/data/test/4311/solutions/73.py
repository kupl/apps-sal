s = int(input())
a = [s]
i = 1
while True:
  if s % 2 == 0:
    s = s // 2
  else:
    s = 3 * s + 1
  if s in a:
    print(len(a) + 1)
    break
  a.append(s)
