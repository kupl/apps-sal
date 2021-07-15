#!/usr/bin/env python3

# from numba import njit

# input = stdin.readline

# @njit
def solve(n,a):
  checkarr = ["o" if a[i] != i+1 else "x" for i in range(n)]
  res = 0
  for i in range(n):
    if checkarr[i] == "x":
      res += 1
      checkarr[i] = "o"
      if i != n-1:
        checkarr[i+1] = "o"
  return res



def main():
  N = int(input())
  # N,M = map(int,input().split())
  a = list(map(int,input().split()))
  print((solve(N,a)))
  return

def __starting_point():
  main()

__starting_point()
