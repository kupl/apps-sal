def solve(n, k):
    return n + k


t = int(input())
for i in range(t):
    n, k = tuple(map(int, input().split()))
    print(solve(n, k))
