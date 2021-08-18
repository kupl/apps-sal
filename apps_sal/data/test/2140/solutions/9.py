

def main():
    S = list(input())
    n = int(input())
    M = sorted(map(int, input().split()))
    R = [0] * len(S)
    for m in M:
        R[m - 1] += 1
    for i in range(len(S) // 2):
        if R[i] % 2 == 1:
            S[i], S[len(S) - i - 1] = S[len(S) - i - 1], S[i]
        R[(i + 1) % len(S)] += R[i]
    print(''.join(S))


def __starting_point():
    main()


__starting_point()
