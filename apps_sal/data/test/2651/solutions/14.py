MOD = 10**9 + 7
def main():
    n, m = map(int, input().split())
    n, m = n-1, m-1
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    a, b = 0, 0
    for i in range(n):
        tmp = (x[i+1] - x[i])
        tmp *= (1+i) * (n-i) % MOD
        a += tmp
        a %= MOD
    for i in range(m):
        tmp = (y[i+1] - y[i])
        tmp *= (1+i) * (m-i) % MOD
        b += tmp
        b %= MOD
    print(a*b % MOD)

def __starting_point():
    main()
__starting_point()
