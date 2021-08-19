(n, m) = list(map(int, input().split()))
streets = [list(map(int, input().split())) for _ in range(n)]
print(max([min(x) for x in streets]))
