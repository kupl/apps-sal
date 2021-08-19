(k, x) = map(int, input().split())
point = [i for i in range(x - k + 1, x + k)]
print(*point)
