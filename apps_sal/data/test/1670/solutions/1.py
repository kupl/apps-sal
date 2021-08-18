"""
Codeforces Contest 281 Div 2 Problem A

Author  : chaotic_iak
Language: Python 3.3.4
"""


def main():
    s1 = read(0)
    s2 = read(0)
    n, = read()
    arr = dict()
    res = []
    for i in range(n):
        w, x, y, z = read(1)
        w = int(w)
        if x + y in arr.keys():
            if arr[x + y][1] != "r":
                res.append((x, y, w))
            arr[x + y] = (w, "r")
        else:
            arr[x + y] = (w, z)
            if arr[x + y][1] == "r":
                res.append((x, y, w))
    for x, y, w in res:
        print(s1 if x == "h" else s2, y, w)


def read(mode=2):
    inputs = input().strip()
    if mode == 0:
        return inputs
    if mode == 1:
        return inputs.split()
    if mode == 2:
        return list(map(int, inputs.split()))


def write(s="\n"):
    if s is None:
        s = ""
    if isinstance(s, list):
        s = " ".join(map(str, s))
    s = str(s)
    print(s, end="")


write(main())
