def main():
    N = int(input())
    S = input()
    cnt = 0
    for i in range(N):
        for j in range(i + 1, N):
            k = 2 * j - i
            if k >= N:
                continue
            if S[j] != S[i] and S[i] != S[k] and S[k] != S[j]:
                cnt += 1
    print((S.count("R") * S.count("B") * S.count("G") - cnt))

def __starting_point():
    main()

__starting_point()
