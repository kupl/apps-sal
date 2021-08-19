# ARC086_B Non Decreasing
def nonDecreasing(N, A):
    Amin = min(A)
    Amax = max(A)
    Amin_index = A.index(Amin) + 1
    Amax_index = A.index(Amax) + 1

    res = []

    # 右をどんどん増やしていく
    # Amaxは正の数のはず
    if abs(Amax) > abs(Amin):
        for i in range(1, N):
            while A[i - 1] > A[i]:
                A[i] += Amax
                res.append((Amax_index, i + 1))
                if A[i] > Amax:
                    Amax = A[i]
                    Amax_index = i + 1

    # 左をどんどん減らしていく
    # Aminは負の数のはず
    else:
        for i in range(N - 1, 0, -1):
            while A[i - 1] > A[i]:
                A[i - 1] += Amin
                res.append((Amin_index, i))
                if A[i - 1] < Amin:
                    Amin = A[i - 1]
                    Amin_index = i
    return res


def __starting_point():
    N = int(input())
    A = list(map(int, input().split()))
    ans = nonDecreasing(N, A)

    print((len(ans)))
    for a in ans:
        print((*a))


__starting_point()
