(a, b) = list(map(int, input().split()))
(c, d) = list(map(int, input().split()))
'\ndef nok(a, b):\n    r = a\n    while r % b != 0:\n        r += a\n    return r\n\ndef get_answer():\n    if b == d:\n        return 0\n\n    if c == a:\n        return -1\n\n    if (b - d) * (c - a) < 0:\n        return -1\n\n    k = nok(abs(b - d), abs(c - a))\n    return b + k * a\n'


def get_answer():
    for i in range(101 * 2):
        for j in range(101 * 2):
            if b + a * i == d + c * j:
                return b + a * i
    return -1


print(get_answer())
