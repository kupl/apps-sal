def main():
    n, k = map(int, input().split())
    mod = 10 ** 9 + 7
    cnt = 0
    for i in range(k, n+2):
        l = (i-1)*i//2
        h = (n+n-i+1)*i//2
        cnt += h - l + 1
    print(cnt % mod)

def __starting_point():
    main()
__starting_point()
