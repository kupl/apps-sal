s = [input(), input()]
pc = [[s[0][i],s[1][i]].count('0') for i in range(len(s[0]))]
ans = 0
for i in range(len(pc) - 1):
  if pc[i] >= 2 and pc[i + 1] >= 1:
    ans += 1
    pc[i] -= 2
    pc[i + 1] -= 1
  elif pc[i] >= 1 and pc[i + 1] >= 2:
    ans += 1
    pc[i] -= 1
    pc[i + 1] -= 2
print(ans)

