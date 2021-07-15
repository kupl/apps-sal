n = int(input())
s = input()

l, r = 0, 0
for i in range(n):
  if s[i] == "(":
    r += 1
  else:
    if r:
      r -= 1
    else:
      l += 1

ans = "("*l + s + ")"*r
print(ans)
