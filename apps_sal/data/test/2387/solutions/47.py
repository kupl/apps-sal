N = int(input())

tleft = 0
tright = 0
a = []
b=  []
for _ in range(N):
  s = input()
  left = 0
  lmin = 0
  for c in s:
    if c == "(":
      left += 1
    else: # ")"
      left -= 1
      lmin = min(lmin,left)
  #
  if left >= 0:
    if lmin == 0:
      tleft += left
    else:
      a.append([left,lmin])
  else:
    if left <= lmin:
      tright += left
    else:
      b.append([left,lmin])
#
a.sort(key=lambda x:-x[1])
b.sort(key=lambda x:x[1])

for left, lmin in a:
  if tleft + lmin < 0:
    print("No")
    return
  else:
    tleft += left
#
for left, lmin in b:
  if tleft + lmin < 0:
    print("No")
    return
  else:
    tleft += left
#
if tleft + tright == 0:
  print("Yes")
else:
  print("No")
#

