from math import*


def main():

    n = int(input())
    ab = [list(map(int, input().split())) for _ in [0] * n]
    k = 10000
    ans2 = 0
    for i in range(k):
        t = 2 * i * pi / k
        s = sin(t)
        c = cos(t)
        ans = [0, 0]
        for a, b in ab:
            if a * s + b * c >= 0:
                ans[0] += a
                ans[1] += b
        ans2 = max(ans2, ans[0]**2 + ans[1]**2)
    print((ans2**0.5))


main()
