3
# -*- coding:utf-8 -*-

import numpy
from collections import defaultdict

def main():
  h, w, d = list(map(int, input().split()))
  mat_a = numpy.array([list(map(int, input().split())) for _ in range(h)])
  q = int(input())
  x_to_pos = dict()
  
  for i in range(h):
    for j in range(w):
      x_to_pos[mat_a[i, j]] = (i, j)
      
  def calc_score(p1, p2):
    return sum([abs(x-y) for x, y in zip(p1, p2)])
  
  visited = numpy.zeros((h, w))
  costs = defaultdict(dict)
  for c in range(1, d+1):
    cost = 0
    costs[c%d][c] = 0
    while True:
      cp = x_to_pos[c]
      c += d
      if c > (h*w):
        break
      np = x_to_pos[c]
      cost += calc_score(cp, np)
      costs[c%d][c] = cost
  
  for _ in range(q):
    l, r = list(map(int, input().split()))
    print((abs(costs[l%d][l] - costs[l%d][r])))

def __starting_point():
  main()


__starting_point()
