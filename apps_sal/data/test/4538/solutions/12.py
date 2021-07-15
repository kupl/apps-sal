N, D = list(map(int, input().split()))

result = 0

for _ in range(N):
    X, Y = list(map(int, input().split()))
    if X * X + Y * Y <= D * D:
        result += 1
print(result)

