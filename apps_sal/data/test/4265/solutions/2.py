s = input()
t = input()

count = 0
for i,j in enumerate(s):
  if j != t[i]:
    count += 1
print(count)
