#!/bin/env python3
# -*- coding: utf-8 -*-

import math


def IS(): return int(input())
def IA(): return [int(x) for x in input().split()]


a, b = IA()

ab = int(str(a) + str(b))
rt = math.sqrt(ab)
print(("Yes" if int(rt) ** 2 == ab else "No"))
