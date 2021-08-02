def main():
    N, M = map(int, input().split())
    bottoms = list(map(int, input().split()))
    lamps = [[0] * N][0]
    for i in range(M):
        for j in range(bottoms[i] - 1, N):
            if lamps[j] == 0:
                lamps[j] = bottoms[i]
    print(' '.join(map(str, lamps)))


main()
