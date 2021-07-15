def solve(n, a):
    res, th = 0, 0
    for x in a:
        th = max(th, x)
        res += th - x
    return res

n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))
