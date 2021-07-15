def main():
    n = int(input())
    inlis = list(map(int, input().split()))

    ans = 10 ** 10

    for kouho1 in range(-100,101):
        tmp1 = 0
        for i in range(n):
            tmp1 += (inlis[i]- kouho1) ** 2
        if tmp1 < ans:
            ans = tmp1
    print(ans)



def __starting_point():
    main()
__starting_point()
