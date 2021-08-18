import sys
input = sys.stdin.readline

q, x = list(map(int, input().split()))

seg_el = 1 << ((x + 1).bit_length())
SEG = [0] * (2 * seg_el)


def add1(n, seg_el):
    i = n + seg_el
    SEG[i] += 1
    i >>= 1

    while i != 0:
        SEG[i] = min(SEG[i * 2], SEG[i * 2 + 1])
        i >>= 1


def getvalues(l, r):
    L = l + seg_el
    R = r + seg_el
    ANS = 1 << 30

    while L < R:
        if L & 1:
            ANS = min(ANS, SEG[L])
            L += 1

        if R & 1:
            R -= 1
            ANS = min(ANS, SEG[R])
        L >>= 1
        R >>= 1

    return ANS


for qu in range(q):
    t = int(input())
    add1(t % x, seg_el)

    MIN = getvalues(0, x)

    OK = 0
    NG = x

    while NG - OK > 1:
        mid = (OK + NG) // 2

        if getvalues(0, mid) > MIN:
            OK = mid
        else:
            NG = mid

    print(MIN * x + OK)
