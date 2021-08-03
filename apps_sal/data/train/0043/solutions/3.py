for _ in range(int(input())):
    n = int(input())
    a = [*list(map(int, input().split()))]
    b = [*list(map(int, input().split()))]
    lo = 0
    hi = sum(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if sum(y if x > mid else 0 for x, y in zip(a, b)) <= mid:
            hi = mid
        else:
            lo = mid + 1
    print(lo)
