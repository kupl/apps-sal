s = input()
t = input()
n = len(t)
out = 2000
for i in range(len(s) - n + 1):
  p = s[i:i+n]
  count = 0
  for j in range(n):
    if t[j] != p[j]:
      count += 1
  if count < out:
    out = count
print(out)
