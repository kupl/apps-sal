def main():
    import bisect

    N = int(input())
    upper = list(map(int, input().split()))
    middle = list(map(int, input().split()))
    lower = list(map(int, input().split()))

    upper.sort()
    middle.sort()
    lower.sort()

    cnt = 0

    for i in range(N):
        mid = middle[i]
        index_up = bisect.bisect_left(upper, mid)
        index_low = bisect.bisect_right(lower, mid)
        
        cnt += index_up * (N - index_low)
    
    print(cnt)


def __starting_point():
    main()
__starting_point()
