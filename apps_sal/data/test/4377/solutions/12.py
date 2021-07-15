# -*- coding: utf-8 -*-

ab, ac, bc, abc = sorted(map(int, input().split()))
print(ab + ac - abc, ab + bc -abc, bc + ac - abc)

