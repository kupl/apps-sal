def main():
    k = int(input())
    (a, b) = list(map(int, input().split()))
    ans = 'NG'
    for i in range(a, b + 1):
        if i % k == 0:
            ans = 'OK'
    return ans


def __starting_point():
    print(main())


__starting_point()
