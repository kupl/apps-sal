(k, x) = map(int, input().split())
print(*list(range(max(x - k + 1, -1000000), min(x + k, 1000001))))
