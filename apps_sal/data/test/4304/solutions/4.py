a, b = map(int, input().split())
n = b - a
sum = 0
for i in range(1, n + 1):
    sum += i
print(sum - b)
