k, s = list(map(int, input().split()))
counter = 0
for i in range(k + 1):
    counter += max(min(k, s - i) - max(0, s - k - i) + 1, 0)

print(counter)
