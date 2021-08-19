import math
(_, a, b) = list(map(int, input().split()))
jet = list(map(int, input().split()))


def jtd(w):
    j = w * a % b
    return j // a


for i in jet:
    print(int(jtd(i)), end=' ')
print()
