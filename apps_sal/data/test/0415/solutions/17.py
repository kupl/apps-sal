n = int(input())
x = list([int(y) - 100 for y in input().split()])
max_time = 0
for i in range(n):
    s = 0
    for j in range(i, n):
        s += x[j]
        if s > 0:
            max_time = max(max_time, j - i + 1)
print(max_time)
