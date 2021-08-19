n = int(input())
a = list(map(int, input().split()))

swaps = []
for i in range(n):
    # find the value at element i
    smallest = a[i]
    best_pos = i
    for j in range(i + 1, n):
        if a[j] < smallest:
            smallest = a[j]
            best_pos = j
    # swap from i to j
    while best_pos > i:
        a[best_pos - 1], a[best_pos] = a[best_pos], a[best_pos - 1]
        swaps.append((best_pos, best_pos + 1))
        best_pos -= 1

for a, b in swaps:
    print(a, b)
