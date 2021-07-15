#!/usr/bin/env python3
import collections, itertools, fractions, functools, heapq, math, queue

def solve():
  a, b = list(map(int, input().split()))
  if a < b:
      return -1
  return (a+b)/(2*((a+b)//(2*b)))

def __starting_point():
  print(solve())


__starting_point()
