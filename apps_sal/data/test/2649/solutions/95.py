N = int(input())

xpy = []
xmy = []


for _ in range(N):
    x, y = map(int, input().split())

    xpy.append(x + y)
    xmy.append(x - y)

print(max(max(xpy) - min(xpy), max(xmy) - min(xmy)))
