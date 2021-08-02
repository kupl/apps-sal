N = int(input())
mini = float('inf')

for i in range(1, 10**6 + 1):
    if N % i == 0:
        mini = min(mini, i + (N // i))

print(mini - 2)
