def main():
    (N, K) = list(map(int, input().split()))
    ans = 0
    dict = {}
    cnt = 0
    tmp = 1 / N
    for i in range(N, 0, -1):
        i = float(i)
        if K <= i:
            ans += tmp * 0.5 ** cnt
        else:
            while True:
                K = K / 2
                cnt += 1
                if K <= i:
                    break
            ans += tmp * 0.5 ** cnt
    return ans


print(main())
