__author__ = 'MoonBall'

import sys
# sys.stdin = open('data/B.in', 'r')
T = 1

def process():
    a = input()
    b = input()
    zero = [0] * 210000

    for i, c in enumerate(a):
        zero[i + 1] = zero[i] + (1 if c == '0' else 0)

    ans = 0
    for i, c in enumerate(b):
        s = max(1, len(a) - (len(b) - i) + 1)
        e = min(i + 1, len(a))
        z = (1 if c == '0' else 0)
        o = 1 - z

        ans += z * (e - s + 1 - (zero[e] - zero[s - 1]))
        ans += o * (zero[e] - zero[s - 1])

    print(ans)








for _ in range(T):
    process()

