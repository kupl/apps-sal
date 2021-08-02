import math


def main():
    n = int(input())
    A = list(map(int, input().split()))
    tmp = A[0]
    oneCnt = 0
    for i in A:
        tmp = math.gcd(tmp, i)
        oneCnt += (i == 1)
    if tmp != 1:
        print(-1)
        return
    if oneCnt > 0:
        print(n - oneCnt)
        return
    ans = 10 ** 8
    for i in range(n):
        tmp = A[i]
        for j in range(i, n):
            tmp = math.gcd(tmp, A[j])
            if tmp == 1:
                ans = min(ans, j - i)
    print(ans + n - 1)


def __starting_point():
    main()


__starting_point()
