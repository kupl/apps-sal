def main():
    n = int(input())
    As = list(map(int, input().split()))
    ans = float('inf')
    for i in range(-100, 101):
        ans_temp = 0
        for j in range(n):
            ans_temp += (As[j] + i) ** 2
        ans = min(ans, ans_temp)
    print(ans)


def __starting_point():
    main()


__starting_point()
