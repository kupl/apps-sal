def main():
    t = int(input())
    for ti in range(t):
        (a, k) = map(int, input().split())
        for i in range(k - 1):
            astr = str(a)
            (mn, mx) = (int(min(astr)), int(max(astr)))
            if mn == 0 or mx == 0:
                break
            a += mn * mx
        print(a)


main()
