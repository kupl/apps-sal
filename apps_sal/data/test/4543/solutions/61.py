#!/bin/env python3
# -*- coding: utf-8 -*-

import math

IS = lambda: int(input())
IA = lambda: [int(x) for x in input().split()]

a, b = IA()

ab = int(str(a) + str(b))
rt = math.sqrt(ab)
print(("Yes" if int(rt) ** 2 == ab else "No"))

