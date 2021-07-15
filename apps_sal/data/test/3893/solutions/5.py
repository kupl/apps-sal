x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
k = 0
n = int(input())
for i in range(n):
    a, b, c = map(int, input().split())
    if (a * x1 + b * y1 + c) * (a * x2 + b * y2 + c) < 0:
        k += 1
print(k)
