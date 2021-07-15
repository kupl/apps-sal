n = int(input())
s = input()
t = ""
for i in range(n):
  t += s[i]
  if t[len(t)-3:] == "fox":
    t = t[:len(t)-3]
print(len(t))
