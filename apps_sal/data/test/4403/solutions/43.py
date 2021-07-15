s = input()
x = 0
for i in range(4):
  if s[i] == "+":
    x += 1
  else:
    x -= 1
print(x)
