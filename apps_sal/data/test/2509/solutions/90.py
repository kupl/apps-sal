def resolve():
    N, K = list(map(int, input().split()))
    cnt = 0
    for b in range(1, N + 1):
        cnt += (N // b) * max(0, b - K) + max(0, N % b - K + 1)
    print(cnt if K != 0 else cnt - N)


if '__main__' == __name__:
    resolve()
