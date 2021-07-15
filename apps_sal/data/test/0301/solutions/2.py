#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Code by H~$~C

from sys import stdin
input = stdin.readline
import math

u, v = map(int, input().split())
if (u == v):
  if (u == 0):
    print(0)
    return
  print(1)
  print(u)
  return
if (u > v):
  print('-1')
  return
if ((v - u) % 2):
  print('-1')
  return

p = (v - u) // 2
if ((u & p) == 0):
  print(2)
  print(p, u + p, sep = ' ')
  return

print(3)
print(u, p, p, sep = ' ')
