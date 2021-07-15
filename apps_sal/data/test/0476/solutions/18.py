s = input()
ss = "144"
i, j = 0, 0
n = len(s)
vale = True
while vale and i < n:
  if j == 3 or s[i] != ss[j]:
    j = 0
  if s[i] != ss[j]:
    vale = False
  j += 1
  i += 1

print("YES" if vale else "NO")

