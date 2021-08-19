def main():
    (N, K) = [int(x) for x in input().split(' ')]
    p = 1000000007
    cnt = 0
    for i in range(K, N + 2):
        cnt = (cnt + i * N - i * i + i + 1) % p
    print(cnt)


main()
