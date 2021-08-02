def solve(n, m):
    s = list(map(int, input().split()))
    if sum(s) == m:
        return 'YES'
    return 'NO'


for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    print(solve(n, m))
