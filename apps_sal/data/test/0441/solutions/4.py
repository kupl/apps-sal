n, a, b = map(int, input().split())
total = a + b
s = input()
prev_took = 'none'
for i in range(n):
  if a == 0 and b == 0:
    break
  if s[i] == '.' and prev_took == 'none':
    if a > b:
      a -= 1
      prev_took = 'a'
    else:
      b -= 1
      prev_took = 'b'
  elif s[i] == '.' and prev_took == 'a':
    if b > 0:
      b -= 1
      prev_took = 'b'
    else:
      prev_took = 'none'
  elif s[i] == '.' and prev_took == 'b':
    if a > 0:
      a -= 1
      prev_took = 'a'
    else:
      prev_took = 'none'
  elif s[i] == '*':
    prev_took = 'none'
print(total - a - b)
