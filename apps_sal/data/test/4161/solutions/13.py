def main():
    import math
    k = int(input())
    cand = [int(v) for v in range(1, k + 1)]
    ans = 0
    for i in range(1, k + 1):
        for j in range(1, k + 1):
            for l in range(1, k + 1):
                temp = math.gcd(i, j)
                res = math.gcd(temp, l)
                ans += res
    return ans


def __starting_point():
    print((main()))


__starting_point()
