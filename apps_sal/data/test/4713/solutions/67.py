N = int(input())
S = list(input())
x = 0
a = [0]

for s in S:
  if s == 'I':
    x += 1
  else:
    x -= 1
  a.append(x)

print(max(a))
