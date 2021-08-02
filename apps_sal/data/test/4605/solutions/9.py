def myfunc(A, B):
    def resfunc(x):
        if A <= sum(map(int, list(str(x)))) <= B:
            return x
        else:
            return 0
    return resfunc


N, A, B = map(int, input().split())
print(sum(map(myfunc(A, B), range(1, N + 1))))
