(a, b) = map(int, input().split())
total = 0
for i in range(1, b - a + 1):
    total += i
print(total - b)
