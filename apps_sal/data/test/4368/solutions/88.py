def main():
    N, K = map(int, input().split())

    if N < K:
        print(1)
        return

    cnt = 0
    while N > 0:
        N = N // K
        cnt += 1

    print(cnt)


main()
