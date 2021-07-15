s = int(input())

box = set()
box.add(s)

for i in range(2, 1000000):
  if s % 2 == 0:
    s //= 2
  else:
    s = s * 3 + 1
  if s in box:
    print(i)
    return
  else:
    box.add(s)

