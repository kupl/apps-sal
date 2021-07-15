n = int(input())
p = list(map(int, input().split(' ')))

if n == 1:
  print(n)
  return

m1 = 0
m2 = 0
ret = 1
max_streak = -1
streak = -1
for i in range(n):
  if p[i] > m1:
    if streak > max_streak:
      max_streak = streak
      ret = m1
    elif streak == max_streak and m1 > 0:
      ret = min(ret, m1)
    m2 = m1
    m1 = p[i]
    streak = -1
  elif p[i] > m2:
    if max_streak < 0:
      ret = p[i]
      max_streak = 0
    elif max_streak == 0:
      ret = min(ret, p[i])
    m2 = p[i]
    streak += 1
  else:
    if max_streak < 0:
      ret = p[i]
      max_streak = 0
    elif max_streak == 0:
      ret = min(ret, p[i])


if streak > max_streak:
  ret = m1
elif streak == max_streak:
  ret = min(ret, m1)

print(ret)
