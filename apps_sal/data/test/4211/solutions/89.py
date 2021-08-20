n = int(input())
b = [*map(int, input().split())]
print(b[0] + sum((min(b[i - 1], b[i]) for i in range(1, n - 1))) + b[-1])
