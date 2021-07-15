#!/usr/bin/env python3

from collections import namedtuple
from itertools   import permutations

Point = namedtuple("Point", "x y")

try:
    while True:
        p = [Point(*list(map(int, input().split()))) for i in range(3)]
        a, b, c = p
        if a.x == b.x == c.x or a.y == b.y == c.y:
            print(1)
        else:
            for a, b, c in permutations(p):
                if a.x == b.x and not a.y < c.y < b.y and not b.y < c.y < a.y:
                    print(2)
                    break
                if a.y == b.y and not a.x < c.x < b.x and not b.x < c.x < a.x:
                    print(2)
                    break
            else:
                print(3)

except EOFError:
    pass

