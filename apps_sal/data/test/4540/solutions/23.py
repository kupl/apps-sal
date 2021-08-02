N = int(input())
a = [0] + list(map(int, input().split())) + [0]
sm = 0
for i in range(1, N + 2):
    sm += abs(a[i - 1] - a[i])
for i in range(1, N + 1):
    print(sm - abs(a[i] - a[i - 1]) - abs(a[i + 1] - a[i]) + abs(a[i - 1] - a[i + 1]))
