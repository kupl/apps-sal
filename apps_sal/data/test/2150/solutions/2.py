#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Code by H~$~C

from sys import stdin
input = stdin.readline
import math

n = int(input())
arr = list(map(int, input().split()))
mx = 0
for i in range(n):
  print(arr[i] + mx, end = ' ')
  mx = max(mx, arr[i] + mx)
print()
