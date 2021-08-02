n = int(input())
x = [0] + list(map(int, input().split())) + [0]
x[0] = 2 * x[1] - x[-2]
x[-1] = 2 * x[-2] - x[1]
for i in range(1, n + 1):
    print(min(x[i] - x[i - 1], x[i + 1] - x[i]), max(x[i] - x[1], x[n] - x[i]))
