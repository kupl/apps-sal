def main():
    N = int(input())
    ans = (N // 11) * 2 
    n = N % 11
    if n > 6:
        ans += 2
    elif n > 0:
        ans += 1
    print(ans)
    
def __starting_point():
    main()
__starting_point()
