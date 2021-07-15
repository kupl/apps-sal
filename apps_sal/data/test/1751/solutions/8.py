def main():
    n = int(input())
    mod = 10**9+7
    f = 1
    for i in range(1,n+1):
        f *= i
        f %= mod

    f -= pow(2,n-1,mod)
    f %= mod
    print(f)

main()

