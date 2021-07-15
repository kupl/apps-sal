N, D = list(map(int, input().split()))
XY = [list(map(int, input().split())) for _ in range(N)]

result = [1 if (((x ** 2 + y ** 2) ** 0.5) <= D) else 0 for x, y in XY]
print((sum(result)))

