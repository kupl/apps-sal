t = int(input())


def yin(a, b):
    if a % b == 0:
        return b
    return yin(b, a % b)


for i in range(0, t):
    (a, b) = map(int, input().split())
    j = yin(max(a, b), min(a, b))
    if j == 1:
        print('Finite')
    else:
        print('Infinite')
