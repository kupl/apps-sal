N, D = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(N)]
print(sum((x**2 + y**2)**.5 <= D for x, y in XY))
