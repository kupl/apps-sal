from sys import stdin

__author__ = 'artyom'


def read_next_line():
  return list(map(int, stdin.readline().strip().split()))


n, a, b = read_next_line()
p, q = read_next_line(), read_next_line()
ans = []
for i in range(1, n + 1):
  ans.append(1 if i in p else 2)

print(' '.join(map(str, ans)))
