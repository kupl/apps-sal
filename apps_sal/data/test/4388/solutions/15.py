s = list(input())
for i in range(3):
  if s[i] == "1":
    s[i] = "9"
  else:
    s[i] = "1"
print("".join(s))
