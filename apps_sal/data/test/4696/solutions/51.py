#!/bin/env python3
# -*- coding: utf-8 -*-

IS = lambda: int(input())
IA = lambda: [int(x) for x in input().split()]

a, b = IA()
print(("Odd" if (a * b) % 2 else "Even"))

