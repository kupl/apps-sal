W, H, N = map(int, input().split())
values = [[0], [W], [0], [H]]
for i in range(N):
    x, y, a = (map(int, input().split()))
    if a <= 2:
        values[a - 1].append(x)
    elif a >= 3:
        values[a - 1].append(y)
print(max(0, min(values[1]) - max(values[0])) * max(0, min(values[3]) - max(values[2])))
