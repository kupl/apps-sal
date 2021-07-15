n, m = list(map(int, input().split()))
heights = list(map(int, input().split()))

neighbors = [[] for i in range(n)]

for i in range(m):
    a, b = list(map(int, input().split()))
    neighbors[a - 1].append(b - 1)
    neighbors[b - 1].append(a - 1)

count = 0
for i in range(n):
    hanamaru = True
    for j in neighbors[i]:
        if heights[i] > heights[j]:
            continue
        else:
            hanamaru = False
            break
    if hanamaru is True:
        count += 1

print(count)

