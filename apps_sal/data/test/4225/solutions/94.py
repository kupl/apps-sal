def easy_linear_programming():
    (A, B, C, K) = map(int, input().split())
    if K <= A:
        print(K)
    elif K - A <= B:
        print(A)
    else:
        k = K - A - B
        print(A - k)


easy_linear_programming()
