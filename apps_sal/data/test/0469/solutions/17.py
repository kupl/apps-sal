#!/bin/python
from math import sqrt

r, h = (int(x) for x in input().split(' '))

# You can always put two in each "row" of the rectangle and one in the dome
in_box = 2 * h // r + 1

# You can add an additional one, like so:
#  O
# O
#
# since they all have radius r/2, you can get the height needed to add an additional one through Pythagorean theorem
remainder = h % r + r
height = r * sqrt(3) / 2 + r

if remainder < height:
	print(in_box)
else:
	print(in_box + 1)
