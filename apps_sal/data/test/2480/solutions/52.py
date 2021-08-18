from collections import defaultdict


def main():
    N, K = list(map(int, input().split()))
    A = list(map(int, input().split()))
    S = [0] * (N + 1)
    for i in range(1, N + 1):
        S[i] = S[i - 1] + A[i - 1]
    T = [(s - i) % K for i, s in enumerate(S)]
    counter = defaultdict(int)
    ans = 0
    for j in range(N + 1):
        if j >= K:
            counter[T[j - K]] -= 1
        ans += counter[T[j]]
        counter[T[j]] += 1
    print(ans)


def __starting_point():
    main()


__starting_point()
