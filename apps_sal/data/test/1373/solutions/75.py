def main():
    n,k = list(map(int,input().split()))
    mod = 10**9+7
    ans = 0
    for i in range(k,n+2):
        ans += (i*(n-i+1)+1) % mod
        ans = ans % mod
    print(ans)

def __starting_point():
    main()

__starting_point()
