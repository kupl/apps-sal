#!/usr/bin/env python3
# -*- coding: utf-8 -*-


n = int(input())
l = list(map(int, input().split()))
if max(l) > 25:
    print(max(l) - 25)
else:
    print(0)
