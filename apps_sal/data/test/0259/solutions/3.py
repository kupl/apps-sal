def main():
    n, t = map(int, input().split())
    mi = 1000000
    ans = 0
    for i in range(n):
        s, d = map(int, input().split())
        L = -1
        R = 1000000
        while R - L != 1:
            M = L + R >> 1
            if s + d * M < t:
                L = M
            else:
                R = M
        if mi > s + d * R:
            mi = s + d * R
            ans = i + 1
    print(ans)
    return 0
main()
