# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 11:29:47 2020

@author: liang
"""

import math

N = int(input())
R = int(math.sqrt(N))
for i in range(R,0,-1):
    if N%i == 0:
        print(len(str(N//i)))
        break
