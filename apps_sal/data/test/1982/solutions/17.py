#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Code by H~$~C

from sys import stdin
input = stdin.readline
import math

for i in range(int(input())):
  n, k = map(int, input().split())
  print(['NO', 'YES'][n >= k * k and (n - k) % 2 == 0])
