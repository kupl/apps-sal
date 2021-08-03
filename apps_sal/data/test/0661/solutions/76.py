def main():
    M, K = list(map(int, input().split()))
    if M == 1:
        if K == 0:
            print('0 0 1 1')
            return
        if K == 1:
            print('-1')
            return
    if (2**M) - 1 < K:
        print('-1')
        return
    l = [i for i in range(K)] + [i for i in range(K + 1, (2**M))] + [K] + [i for i in reversed(list(range(K + 1, (2**M))))] + [i for i in reversed(list(range(K)))] + [K]
    print((' '.join(str(i) for i in l)))


main()
