def __starting_point():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    cnt = 0
    result = 1145141919
    res1 = A * (N - 1)
    res2 = B * (N - 1)
    if (N >= 2):
        res3 = min(A, B) + C * (N - 2)
        result = min(result, res3)
    result = min(result, res1, res2)
    print (result)

__starting_point()
