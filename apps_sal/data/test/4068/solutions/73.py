def main():
    (N, M) = list(map(int, input().split()))
    mod = 10 ** 9 + 7
    a = [0] * (N + 1)
    a[0] = 1
    banned = [False] * (N + 1)
    for x in range(M):
        n = int(input())
        banned[n] = True
    for i in range(1, N + 1):
        res = 0
        if not banned[i - 1]:
            res += a[i - 1]
        if not banned[i - 2]:
            res += a[i - 2]
        a[i] = res
    print(a[-1] % mod)
    return


main()
