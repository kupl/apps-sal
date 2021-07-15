r, D, x = list(map(int, input().split()))

for i in range(10):
    next_x = (r * x) - D
    print(next_x)
    x = next_x

