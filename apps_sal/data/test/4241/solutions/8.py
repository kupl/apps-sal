l1 = input()
l2 = input()
n_steps = []

for i in range(len(l1) - len(l2) + 1):
  num = 0
  for i, l in enumerate(l2):
    if l1[i] != l:
      num += 1
  n_steps.append(num) 
  l1 = l1[1:]
n_steps.sort()
print((n_steps[0]))


