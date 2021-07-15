from collections import namedtuple
from itertools   import permutations

Rect = namedtuple("Rect", "h w c")

def rotations(r):
    yield r
    yield Rect(r[1], r[0], r[2])

def main():
    a, b, c, d, e, f = map(int, input().split())
    a = Rect(a, b, 'A')
    b = Rect(c, d, 'B')
    c = Rect(e, f, 'C')
    del d, e, f
    for a0 in rotations(a):
        for b0 in rotations(b):
            for c0 in rotations(c):
                for x, y, z in permutations((a0, b0, c0), 3):
                    if x.w == y.w == z.w == x.h + y.h + z.h:
                        # AAA
                        # BBB
                        # CCC
                        print(x.w)
                        for i in range(x.h):
                            print(x.c * x.w)
                        for i in range(y.h):
                            print(y.c * y.w)
                        for i in range(z.h):
                            print(z.c * z.w)
                        return
                    elif x.w == y.w + z.w == x.h + y.h and y.h == z.h:
                        # AAA
                        # BBC
                        # BBC
                        print(x.w)
                        for i in range(x.h):
                            print(x.c * x.w)
                        for i in range(y.h):
                            print(y.c * y.w, end="")
                            print(z.c * z.w)
                        return
    print(-1)

main()

