from itertools import product
n = int(input())
ans = 0

for i in range(3, len(str(n))+1):
  for t in product(['3', '5', '7'], repeat=i):
    s = "".join(t)
    if 1 <= int(s) <= n and len(set(s)) == 3:
      ans += 1

print(ans)
