import sys


def input():
    return sys.stdin.readline()[:-1]


t = int(input())
for _ in range(t):
    n = int(input())
    c = list(map(int, input().split()))
    if n == 1:
        print(1, c[0], 0)
        continue
    M = c[0]
    l, r = 1, n
    a, b = c[0], 0
    for i in range(1, 1000000):
        if i % 2 == 0:
            a_tmp = 0
            while a_tmp <= M and l < r:
                a_tmp += c[l]
                a += c[l]
                l += 1
            if l == r:
                break
            M = a_tmp
        else:
            b_tmp = 0
            while b_tmp <= M and l < r:
                b_tmp += c[r - 1]
                b += c[r - 1]
                r -= 1
            if l == r:
                break
            M = b_tmp
    print(i + 1, a, b)
