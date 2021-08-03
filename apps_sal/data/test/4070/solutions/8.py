"""
Codeforces April Fools Contest 2017 Problem B

Author  : chaotic_iak
Language: Python 3.5.2
"""

# SOLUTION


def main():
    n, = read()
    n = hex(n).upper()[2:]
    dc = [1, 0, 0, 0, 1, 0, 1, 0, 2, 1, 1, 2, 0, 1, 0, 0]
    sm = 0
    for c in n:
        if ord(c) < 58:
            sm += dc[ord(c) - 48]
        else:
            sm += dc[ord(c) - 65 + 10]
    print(sm)

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
