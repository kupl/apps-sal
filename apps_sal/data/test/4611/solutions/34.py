t, x, y = 0, 0, 0

for i in range(int(input())):
    t_n, x_n, y_n = map(int, input().split())
    diff = abs(x - x_n) + abs(y - y_n)
    if diff > t_n - t or (t_n - t - diff) % 2 == 1:
        print("No")
        return
    t, x, y = t_n, x_n, y_n
print("Yes")
