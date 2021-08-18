"""
Codeforces Round 427 Div 2 Problem A

Author  : chaotic_iak
Language: Python 3.5.2
"""


def main():
    s, v1, v2, t1, t2 = read()
    l1 = v1 * s + t1 * 2
    l2 = v2 * s + t2 * 2
    if l1 < l2:
        return "First"
    if l1 > l2:
        return "Second"
    return "Friendship"


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
