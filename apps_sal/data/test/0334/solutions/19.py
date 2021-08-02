a, b = list(map(int, input().split()))
c, d = list(map(int, input().split()))

"""
def nok(a, b):
    r = a
    while r % b != 0:
        r += a
    return r

def get_answer():
    if b == d:
        return 0

    if c == a:
        return -1

    if (b - d) * (c - a) < 0:
        return -1

    k = nok(abs(b - d), abs(c - a))
    return b + k * a
"""


def get_answer():
    for i in range(101 * 2):
        for j in range(101 * 2):
            if b + a * i == d + c * j:
                return b + a * i

    return -1


print(get_answer())
