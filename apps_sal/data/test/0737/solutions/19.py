n = int(input())
x = 10**6
y = x
for i in range(1, n + 1):
    if x + y > i + ((n - 1) // i + 1):
        x = ((n - 1) // i + 1)
        y = i
print(2 * (x + y))
