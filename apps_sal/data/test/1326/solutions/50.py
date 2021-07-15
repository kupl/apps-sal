def solve():
    N = int(input())
    ans = 0
    for k in range(1, N+1):
        x = N // k
        ans += x * (k + x*k) // 2
    print(ans)

def __starting_point():
    solve()
__starting_point()
