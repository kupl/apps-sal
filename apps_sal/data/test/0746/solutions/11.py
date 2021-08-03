a, b = list(map(int, input().split()))
n = int(input())
time = -1
for i in range(n):
    x, y, v = list(map(int, input().split()))
    t = ((a - x)**2 + (b - y)**2)**0.5 / v
    if time == -1 or t < time:
        time = t
print(time)
