S = input()[::-1]
ans = 0
mods = [0] * 2019
mods[0] = 1
current = 0
x = 1
for s in S:
  current = (current + x * int(s)) % 2019
  ans += mods[current % 2019]
  mods[current % 2019] += 1
  x = x * 10 % 2019
print(ans)
