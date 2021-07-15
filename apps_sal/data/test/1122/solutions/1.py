def main():
    n, m = map(int, input().split())
    if n%2:
        for i in range(m):
            print(i+1, n-i)
    else:
        for i in range(m):
            if n-2*i-1 > n//2:
                print(i+1, n-i)
            else:
                print(i+1, n-i-1)

def __starting_point():
    main()
__starting_point()
