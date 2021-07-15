s = input()
n = 0
for i in range(4):
  if s[i] == '+': n += 1
  if s[i] == '-': n -= 1
print(n)
