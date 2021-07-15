# 441C

__author__ = 'artyom'

n, m, k = map(int, input().split())
i, j, d, t = 1, 1, 1, 1
ans = ''


def get_next(x, y, dir):
  y += dir
  if y > m:
    y = m
    x += 1
    dir = -1
  if y == 0:
    y = 1
    x += 1
    dir = 1
  return x, y, dir


while t < k:
  ans += '2 ' + str(i) + ' ' + str(j)
  i, j, d = get_next(i, j, d)
  ans += ' ' + str(i) + ' ' + str(j) + '\n'
  i, j, d = get_next(i, j, d)
  t += 1
rem = n * m - (t - 1) * 2
ans += str(rem)
while rem > 0:
  ans += ' ' + str(i) + ' ' + str(j)
  i, j, d = get_next(i, j, d)
  rem -= 1

print(ans)
