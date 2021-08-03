#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

place = input()

start = time.time()

if place == 'a1' or place == 'a8' or place == 'h1' or place == 'h8':
    ans = 3
elif place[0] == 'a' or place[0] == 'h' or place[1] == '1' or place[1] == '8':
    ans = 5
else:
    ans = 8
print(ans)
finish = time.time()
#print(finish - start)
