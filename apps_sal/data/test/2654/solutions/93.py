3
# -*- coding:utf-8 -*-

import numpy

def main():
  n = int(input())
  la, lb = [], []
  for _ in range(n):
    a, b = list(map(int, input().split()))
    la.append(a)
    lb.append(b)
  la.sort(), lb.sort()
  
  if n % 2 == 0:
    s = (n-1)//2
    e = s + 2
    ma = sum(la[s:e]) / 2.0
    mb = sum(lb[s:e]) / 2.0
    print((int(2 * (mb - ma) + 1)))
  if n % 2 == 1:
    ma = la[n//2]
    mb = lb[n//2]
    print((mb - ma + 1))
    
def __starting_point():
  main()


__starting_point()
