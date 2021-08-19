(N, D) = map(int, input().split())
X = [input() for i in range(N)]


def ans174(N: int, D: int, X: list):
    count = 0
    import math
    for i in range(N):
        X_list = list(map(int, X[i].split()))
        if math.sqrt(X_list[0] ** 2 + X_list[1] ** 2) <= D:
            count += 1
    return count


print(ans174(N, D, X))
