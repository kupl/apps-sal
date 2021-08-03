s = 0
n = int(input())
for i in range(n):
    x, y = list(map(float, input().split()))
    s += y
print(s / n + 5)
