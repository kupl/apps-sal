# 0 1 2  3  4  5
# 1 2 4  7 11 16

def f(x):
    return x * (x + 1) // 2


def works(n, k, s):
    rem = k - 1 - s
    val = f(k - 1) - f(rem) + 1

    return val >= n


def main():
    n, k = list(map(int, input().split()))
    if n == 1:
        print(0)
    else:
        if not works(n, k, k):
            print(-1)
        else:
            lo = 0
            hi = k
            while lo + 1 < hi:
                mid = (lo + hi) // 2
                if works(n, k, mid):
                    hi = mid
                else:
                    lo = mid
            print(hi)


main()
