def main():
    a, b, k = list(map(int, input().split()))
    ans = []
    count = 0
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            ans.append(i)
    print(ans[k*-1])


def __starting_point():
    main()
__starting_point()
