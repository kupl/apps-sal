def __starting_point():
    #n, m = list(map(int, input().split()))
    n = int(input())
    print(n // 7 * 2 + (1 if n % 7 > 5 else 0), n // 7 * 2 + (2 if n % 7 >= 2 else n % 7))
    

__starting_point()
