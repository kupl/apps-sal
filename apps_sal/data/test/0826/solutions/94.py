def solve():
    N = int(input())

    left = 1
    right = N+1

    while right - left > 1:
        mid = (left+right) // 2
        if (mid*(mid+1)) // 2 > N+1:
            right = mid
        else:
            left = mid
    
    print((N-left+1))

def __starting_point():
    solve()

__starting_point()
