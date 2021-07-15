def main():
    n = int(input())
    k = int(input())
    x = int(input())
    y = int(input())

    if n <= k :
        ans = x * n
    else :
        ans = x * k + y * (n - k)

    print(ans)



def __starting_point():
    main()

__starting_point()
