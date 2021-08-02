import sys
mod = 10**9 + 7


def LI(): return [int(x) for x in sys.stdin.readline().split()]


def main():
    n, l, r = LI()
    a = [1, 0, 0]
    t = [0, 0, 0]
    k = r // 3
    t = [k] * 3
    if r % 3 > 0:
        t[1] += 1
    if r % 3 > 1:
        t[2] += 1
    k = l // 3
    t = [c - k for c in t]
    if l % 3 == 0:
        t[0] += 1
    if l % 3 > 1:
        t[1] -= 1

    for _ in range(n):
        u = [0] * 3
        for i in range(3):
            k = a[i]
            for j in range(3):
                u[(i + j) % 3] += k * t[j] % mod
        a = [c % mod for c in u]

    return a[0]


print(main())
