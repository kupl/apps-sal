a, b = list(map(int, input().split()))

d = b - a

print(d * (d+1) // 2 - b)
