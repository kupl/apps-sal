A, B = map(str, input().split())
l = list(range(int(A), int(B)+1))
c = 0
for i in l:
  t = str(i)
  if t[0] == t[4] and t[1] == t[3]:
    c += 1
print(c)
