def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    A = [1 / a for a in A]
    print(1 / sum(A))
    return


solve()
