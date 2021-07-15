def __starting_point():

    n,k = list(map(int,input().split()))

    A = [0] * n

    for _ in range(k):
        m = int(input())
        B = list(map(int,input().split()))
        for b in B:
            A[b-1] += 1
    print((A.count(0)))

__starting_point()
