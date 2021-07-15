def solve():
    N = int(input())
    A = [int(s) for s in input().split()]
    A = A[::-1]
    print(*A)
    return

T = int(input())
for t in range(T):
    solve()

