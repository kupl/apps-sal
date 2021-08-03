def solve(ps):
    return max(
        max(ps, key=lambda x: x[0])[0] - min(ps, key=lambda x: x[0])[0],
        max(ps, key=lambda x: x[1])[1] - min(ps, key=lambda x: x[1])[1],
    )**2


n = int(input())
ps = [list(map(int, input().split())) for i in range(n)]
print(solve(ps))
