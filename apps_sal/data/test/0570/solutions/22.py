# coding: utf-8

import math


vs = ["Vladik", "Valera"]
a, b = list(map(int, input().split(" ")))

an = math.floor(math.sqrt(a))
bn = 0
while True:
    bn += 1
    if b < bn * (bn + 1):
        bn -= 1
        break

print(vs[an > bn])
