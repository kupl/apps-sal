n = int(input())
c = input()

w = c.count("W")
r = c.count("R")

ans = 0
for i in range(r):
  if c[i] == "W": ans += 1
print(ans)
