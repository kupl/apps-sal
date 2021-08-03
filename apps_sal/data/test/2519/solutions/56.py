def main():
    N, K = [int(x) for x in input().split(" ")]
    P = [int(p) for p in input().split(" ")]
    E = [sum(P[:K])]
    for i in range(N - K):
        E.append(E[-1] - P[i] + P[i + K])
    print((max(E) + K) / 2)


main()
