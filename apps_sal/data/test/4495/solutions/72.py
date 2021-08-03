import re
import copy


def accept_input():
    a, b, x = list(map(int, input().split()))
    return a, b, x


a, b, x = accept_input()
print((b // x - (a - 1) // x))
"""
if a%x == 0 and a != b:
    print(b//x - a//x +1)
elif a%x == 0 and a == b:
    print(0)
else:
    print(b//x - a//x)
"""
