n = int(input())
s = input()
t = ""
x = 0
for i in range(n):
  t += s[i]
  x += 1
  if x >= 3 and t[-3:] == "fox":
    t = t[:-3]
    x -= 3

ans = len(t)
print(ans)

