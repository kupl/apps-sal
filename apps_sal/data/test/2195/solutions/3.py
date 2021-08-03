def solve(x, y, a, b):
    if b >= a * 2:
        return (x + y) * a
    else:
        return min(x, y) * b + (max(x, y) - min(x, y)) * a


[print(solve(*map(int, input().split()), *map(int, input().split()))) for _ in range(int(input()))]
