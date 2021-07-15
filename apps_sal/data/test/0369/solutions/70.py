n, m = map(int, input().split())
s = input()
roulette = []

cur = n
while cur > m:
  for a in range(m):
    if s[cur - m + a] == '0':
      roulette.append(m - a)
      cur = cur - m + a
      break
  else:
    print(-1)
    break
else:
  roulette.append(cur)
  print(' '.join(map(str, roulette[::-1])))
