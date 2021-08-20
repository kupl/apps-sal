import re
import copy


def accept_input():
    (a, b, x) = list(map(int, input().split()))
    return (a, b, x)


(a, b, x) = accept_input()
print(b // x - (a - 1) // x)
'\nif a%x == 0 and a != b:\n    print(b//x - a//x +1)\nelif a%x == 0 and a == b:\n    print(0)\nelse:\n    print(b//x - a//x)\n'
