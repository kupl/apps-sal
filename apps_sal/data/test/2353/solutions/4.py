def solve(a, b, c, d):
    if b >= a:
        return b
    if d >= c:
        return -1
    return b + (a - b + c - d - 1) // (c - d) * c


[print(solve(*map(int, input().split()))) for _ in range(int(input()))]
