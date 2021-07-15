def main():
    import sys
    input = sys.stdin.readline

    n, m = map(int, input().split())
    l = 1
    r = n
    if n % 2 == 1:
        for i in range(m):
            print(f"{l} {r}")
            l += 1
            r -= 1
    else:
        flag = True
        for i in range(m):
            if flag and r - l <= n // 2:
                r -= 1
                flag = False
            print(f"{l} {r}")
            l += 1
            r -= 1


main()
