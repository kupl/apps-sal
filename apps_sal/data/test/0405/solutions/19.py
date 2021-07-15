n = int(input())
bumps = input()

ans = 0

for i in range(n):
  if bumps[i] == ">":
    ans += i
    break
else:
  ans += n

for i in range(n):
  if bumps[n - 1 - i] == "<":
    ans += i
    break
else:
  ans += n

print(ans)
