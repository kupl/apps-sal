"""
Codeforces April Fools Contest 2017 Problem E

Author  : chaotic_iak
Language: Python 3.5.2
"""


def main():
    a, = read()
    b, = read()
    c, = read()
    d, = read()
    n = 8 * a + 4 * b + 2 * c + d

    dc = {0: 0,
          1: 1,
          2: 0,
          3: 1,
          4: 0,
          5: 0,
          6: 0,
          7: 0,
          8: 1,
          9: 1,
          10: 0,
          11: 1,
          12: 1,
          13: 0,
          14: 1,
          15: 1,
          }
    print(dc[n])


def read(callback=int):
    return list(map(callback, input().strip().split()))


def write(value, end="\n"):
    if value is None:
        return
    try:
        if not isinstance(value, str):
            value = " ".join(map(str, value))
    except:
        pass
    print(value, end=end)


write(main())
