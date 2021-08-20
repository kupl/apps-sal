import sys
input = sys.stdin.readline


def fa(a1, b2, a2, b3, a3, b1):
    c = 0
    bv = max(b1 - a1 - a2, 0)
    c = c + bv
    a2 = a2 - b1
    if a2 < 0:
        a1 = max(a1 + a2, 0)
        a2 = 0
    bv = max(b2 - a2 - a3, 0)
    c = c + bv
    a2 = a2 - b2
    if a2 < 0:
        a3 = max(a2 + a3, 0)
    bv = max(b3 - a1 - a3, 0)
    c = c + bv
    return c


def main():
    n = int(input())
    (a1, a2, a3) = list(map(int, input().split()))
    (b1, b2, b3) = list(map(int, input().split()))
    v = min(a1, b2) + min(a2, b3) + min(a3, b1)
    c = min(fa(a1, b2, a2, b3, a3, b1), fa(a1, b2, a3, b1, a2, b3), fa(a2, b3, a1, b2, a3, b1), fa(a2, b3, a3, b1, a1, b2), fa(a3, b1, a1, b2, a2, b3), fa(a3, b1, a2, b3, a1, b2))
    print(c, v)


main()
