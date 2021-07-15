s = [i for i in input()]
t = [j for j in input()]
count = 0
for k in range(3):
  if s[k] == t[k]:
    count += 1
print(count)
