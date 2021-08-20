(n, m) = map(int, input().split())
print(max((min(map(int, input().split())) for i in range(n))))
