def main():
    n = int(input())
    ans = n*(n-1)*(n-2)*(n-3)*(n-4) // (5*4*3*2*1)
    ans *= 120 * ans
    print(ans)

def __starting_point():
    main()
__starting_point()
