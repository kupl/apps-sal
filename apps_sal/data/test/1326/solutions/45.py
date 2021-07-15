def main():
    n = int(input())
    ans = 0
    for k in range(1,n+1):
        ans += k * (n//k) * (n//k+1) //2
    print(ans)

def __starting_point():
    main()

__starting_point()
