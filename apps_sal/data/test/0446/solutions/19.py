def main():
    n = int(input())
    k = 1
    num = 1
    ans = 1
    while num <= n:
        num = (2 ** k - 1) * 2 ** (k - 1)
        if n % num == 0:
            ans = num
        k += 1
    print(ans)


main()
