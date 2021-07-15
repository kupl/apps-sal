s = list(input())
c = 0
ans = [0]

for i in s:
  if i == 'A' or i == 'C' or i == 'G' or i == 'T':
    c += 1
  else:
    c = 0
  ans.append(c)

print(max(ans))
