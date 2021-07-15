s = input()
ans = 753
for i in range(len(s) - 2):
  x = int(s[i:i+3])
  if abs(753 - x) < ans:
    ans = abs(753-x)
print(ans)
