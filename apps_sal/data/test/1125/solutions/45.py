def main():
    n = int(input())
    a = list(map(int, input().split()))
    (x, y) = (a[0], a[1])
    nim = 0
    for i in range(2, n):
        nim ^= a[i]
    ans = 0
    while x ^ y != nim:
        for i in range(50, -1, -1):
            j = nim >> i & 1
            xy = (x >> i ^ y >> i) & 1
            if j != xy:
                m = min(x % 2 ** i + 1, 2 ** i - y % 2 ** i)
                if x % 2 ** i + 1 == 2 ** i - y % 2 ** i:
                    print(-1)
                    return
                x -= m
                y += m
                ans += m
                if x <= 0:
                    print(-1)
                    return
                break
        else:
            if x ^ y != nim:
                print(-1)
                return
    print(ans)


main()
