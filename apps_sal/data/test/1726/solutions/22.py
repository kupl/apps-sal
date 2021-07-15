# -*- coding: utf-8 -*-

def f(t, arr):

  mtime = 86400
  
  r = 1
  for x in arr:
    t -= mtime - x
    if t <= 0:
      break
    r += 1

  print(r)


def __starting_point():
  
  n, t = list(map(int, input().split()))
  arr = list(map(int, input().split()))

  # for i in range(n):
  #   list(map(int, input().split()))

  f(t, arr)
__starting_point()
