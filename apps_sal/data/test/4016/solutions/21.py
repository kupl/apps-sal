(N, K) = list(map(int, input().split()))
T = input()


def findAns(N, T):
    for i in range(N - 1):
        if T[i + 1:] == T[:N - 1 - i]:
            return T[N - 1 - i:]
    return T


ans = findAns(N, T)
print(T + ans * (K - 1))
