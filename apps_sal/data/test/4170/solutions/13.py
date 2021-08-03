n = int(input())
high = list(map(int, input().split()))

a = []
count = 0

for x in range(n - 1):
    if high[x] - high[x + 1] >= 0:
        count += 1
    else:
        a.append(count)
        count = 0
a.append(count)

print((max(a)))
