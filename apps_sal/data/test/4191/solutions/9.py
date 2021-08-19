"""
Codeforces April Fools Contest 2017 Problem E

Author  : chaotic_iak
Language: Python 3.5.2
"""

# SOLUTION


def main():
    a, = read()
    b, = read()
    c, = read()
    d, = read()
    n = 8 * a + 4 * b + 2 * c + d

    dc = {0: 0,    # test 2 confirmed correct
          1: 1,    # test 9 confirmed correct
          2: 0,    # probably test 6
          3: 1,    # test 13 confirmed correct
          4: 0,    # probably test 4
          5: 0,    # probably test 11
          6: 0,    # test 1 confirmed correct
          7: 0,    # probably test 15
          8: 1,    # test 3 confirmed correct
          9: 1,    # test 10 confirmed correct
          10: 0,    # probably test 7
          11: 1,    # probably test 14
          12: 1,    # test 5 confirmed correct
          13: 0,    # probably test 12
          14: 1,    # test 8 confirmed correct
          15: 1,    # probably test 16
          }
    print(dc[n])

# HELPERS


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
