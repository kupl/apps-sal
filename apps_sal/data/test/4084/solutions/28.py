def main():
    n, a, b = map(int, input().split())
    quo = n // (a+b)
    rem = n % (a+b)
    ans = quo * a
    if a >= rem:
        ans += rem
    else:
        ans += a
    print(ans)
    
def __starting_point():
    main()
__starting_point()
