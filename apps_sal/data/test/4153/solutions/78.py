s = list(input())
n = len(s)
t = []
while s:
  c = s.pop()
  if t and t[-1] != c:
    t.pop()
  else:
    t.append(c)
print(n - len(t))
