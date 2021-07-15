n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
plus = [p[0] + p[1] for p in points]
minus = [p[0] - p[1] for p in points]
print(max(max(plus) - min(plus), max(minus) - min(minus)))
