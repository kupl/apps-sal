s = input()
cnt = [0]*4
ind = [0]*4
for i, ch in enumerate(s):
  if ch == "R": ind[0] = i % 4
  elif ch == "B": ind[1] = i % 4
  elif ch == "Y": ind[2] = i % 4
  elif ch == "G": ind[3] = i % 4
  else: cnt[i % 4] += 1
print(*[cnt[ind[i]] for i in range(4)])  

