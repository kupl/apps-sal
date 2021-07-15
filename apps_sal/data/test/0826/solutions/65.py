def solve():
    N = int(input())

    ng = N+1
    ok = 1

    while abs(ng-ok) > 1:
        mid = (ok+ng) // 2
        if mid*(mid+1)//2 <= N+1:
            ok = mid
        else:
            ng = mid
    
    print((N-ok+1))
def __starting_point():
    solve()

__starting_point()
