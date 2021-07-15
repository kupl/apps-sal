from bisect import bisect_left

def main():
    N, M, X = list(map(int, input().split()))
    A = list(map(int, input().split()))
    mid = bisect_left(A, X)
    l = len(A[:mid])
    r = len(A[mid:])
    print((min(l, r)))

def __starting_point():
    main()

__starting_point()
