k, x = map(int, input().split())

y = []

for i in range((x - (k - 1)), (x + k)):
    if -1000000 < i and i < 1000000:
        y.append(i)
print(' '.join(map(str, y)))
