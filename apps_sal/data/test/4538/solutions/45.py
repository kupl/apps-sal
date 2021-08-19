(n, d) = map(int, input().split())
print(sum([x * x + y * y <= d * d for (x, y) in [map(int, input().split()) for i in range(n)]]))
