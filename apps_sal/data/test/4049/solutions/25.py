import sys


def main():
    n = int(sys.stdin.readline().strip())
    (a, a1, a2) = list(map(int, sys.stdin.readline().split()))
    (b, b1, b2) = list(map(int, sys.stdin.readline().split()))
    res = min(a, b1) + min(a1, b2) + min(a2, b)
    if b >= a1 + a:
        ans = a2 - (n - b)
    elif b1 >= a1 + a2:
        ans = a - (n - b1)
    elif b2 >= a2 + a:
        ans = a1 - (n - b2)
    elif b == a and b1 == a1 and (b2 == a2):
        ans = 0
    elif a > b and a1 > b1:
        b2 -= a2
        a -= b2
        a1 -= b1
        if a <= 0:
            ans = a1 - b
        else:
            ans = a + a1 - b
    elif a2 > b2 and a1 > b1:
        b -= a
        a1 -= b
        a2 -= b2
        if a1 <= 0:
            ans = a2 - b1
        else:
            ans = a2 + a1 - b1
    elif a > b and a2 > b2:
        b1 -= a1
        a2 -= b1
        a -= b
        if a2 <= 0:
            ans = a - b
        else:
            ans = a2 + a - b
    elif a > b:
        a -= b
        b1 -= a1
        a2 -= b1
        a1 = 0
        ans = a + a2 - b2
    elif a1 > b1:
        a1 -= b1
        b2 -= a2
        a -= b2
        a2 = 0
        ans = a + a1 - b
    elif a2 > b2:
        a2 -= b2
        b -= a
        a1 -= b
        a = 0
        ans = a2 + a1 - b1
    print(max(0, ans), res)


for i in range(1):
    main()
