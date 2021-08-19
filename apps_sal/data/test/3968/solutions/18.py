#!/usr/bin/env python3
# -*- coding: utf-8 -*-

input()
a = sorted(map(int, input().split()))[::-1]
a[1:1] = a.pop(),
print(*a)
