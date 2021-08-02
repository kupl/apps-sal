n = int(input())
x = list(map(int, input().split()))

print(x[1] - x[0], x[n - 1] - x[0])
for i in range(1, n - 1):
    print(min(x[i + 1] - x[i], x[i] - x[i - 1]), max(x[n - 1] - x[i], x[i] - x[0]))
print(x[n - 1] - x[n - 2], x[n - 1] - x[0])
