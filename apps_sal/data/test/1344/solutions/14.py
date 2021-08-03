#!/usr/bin/env	python
# -*-coding:utf-8 -*-
import sys
import io
import os
import math
import copy
import pickle
n = int(input())
M = tuple(map(int, input().split()))
s = m = 0
for i in range(1, n):
    if M[i - 1] < M[i]:
        s = max(s, i - m)
    else:
        m = i
print(1 + s)
