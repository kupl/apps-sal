#!/usr/bin/env python3
import heapq
# input = stdin.readline

def solve(n,m,a):
  a = [-x for x in a]
  heapq.heapify(a)
  for _ in range(m):
    x = heapq.heappop(a)
    heapq.heappush(a,-(abs(x)//2))
  return abs(sum(a))


def main():
  N,M = list(map(int,input().split()))
  a = list(sorted(map(int,input().split())))
  print((solve(N,M,a)))
  pass

def __starting_point():
  main()

__starting_point()
