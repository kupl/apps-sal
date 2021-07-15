#!/usr/bin/env python3

# input = stdin.readline


def main():
  A,B = list(map(int,input().split()))
  def primeLst(x):
    acc = []
    f = 2
    while f * f <= x:
      if x % f == 0:
        acc.append(f)
        x //= f
      else:
        f += 1
    if x != 1:
      acc.append(x)
    return acc
  a = set(primeLst(A))
  b = set(primeLst(B))
  if len(a) * len(b) == 0:
    ans = 1
  else:
    ans = len(a&b) + 1
  print(ans)
  return

def __starting_point():
  main()

__starting_point()
