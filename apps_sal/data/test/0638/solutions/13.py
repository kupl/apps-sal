import sys 
read = lambda : sys.stdin.readline().strip()
write = lambda x: sys.stdout.write(x)

n, m = map(int, input().split())
t = list(map(int, input().split()))

ans = [0]

for k in range(1, n):
  a = sorted(t[:k])
  s = [t[k], -1]
  for j, i in enumerate(a):
    if s[0] + i > m:
      s[1] = j
      break
    else:
      s[0] += i
  if s[1] == -1:
    ans.append(0)
  else:
    ans.append(k - s[1])

  #print(k, s)
print(*ans)
