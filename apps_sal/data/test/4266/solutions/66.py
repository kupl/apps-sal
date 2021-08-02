K, X = map(int, input().split())


def ans137(K: int, X: int):
    ansstr = ""
    for i in range(-1000000, 1000000):
        if abs(X - i) < K:
            ansstr += str(i) + " "
    return ansstr[:-1]


print(ans137(K, X))
