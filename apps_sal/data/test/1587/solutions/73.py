N = int(input())
c = input()

R_r = c.count("R")
W_l = 0
ans = N
for i in range(N+1):
  t = max(R_r,W_l)
  ans = min(ans, t)
  if R_r == 0:
    break
  if c[i] == "R":
    R_r -= 1
  else:
    W_l += 1

print(ans)
