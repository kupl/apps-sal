s = input()
t = input()
a = [0] * 26
for c in s:
  a[ord(c) - ord('a')] += 1
b = [0] * 26
for c in t:
  b[ord(c) - ord('a')] += 1
if any(a[i] < b[i] for i in range(26)):
  print("need tree")
else:
  needAutomaton = (len(s) > len(t))
  needArray = False
  j = 0
  for i in range(len(t)):
    k = s.find(t[i], j)
    if k < j:
      needArray = True
      break
    j = k + 1
  if needAutomaton and needArray:
    print("both")
  elif needAutomaton:
    print("automaton")
  else:
    print("array")
