import copy


def FindParent(X):
    if Parent[X] == X:
        return X
    else:
        Parent[X] = FindParent(Parent[X])
        return Parent[X]


def UniteParent(X, Y):
    X = FindParent(X)
    Y = FindParent(Y)
    if X == Y:
        return 0
    if Rank[X] < Rank[Y]:
        Parent[X] = Y
    else:
        Parent[Y] = X
        if Rank[X] == Rank[Y]:
            Rank[X] += 1


N, M = (int(T) for T in input().split())
List = [[] for TM in range(0, M)]
for TM in range(0, M):
    List[TM] = [int(T) for T in input().split()]

Count = 0
for TM in range(0, M):
    ListCopy = copy.deepcopy(List)
    del ListCopy[TM]

    Parent = [I for I in range(N + 1)]
    Rank = [0] * (N + 1)
    for TTM in range(0, M - 1):
        UniteParent(ListCopy[TTM][0], ListCopy[TTM][1])
    for TN in range(1, N + 1):
        FindParent(TN)
    if len(set(Parent[1:])) > 1:
        Count += 1
print(Count)
