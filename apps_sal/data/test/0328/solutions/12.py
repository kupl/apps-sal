num_points = int(input())
solution = 0
for _ in range(num_points):
    (x, y) = list(map(int, input().split()))
    solution = max(solution, x + y)
print(solution)
