n = int(input())
a = list(map(int, input().split()))

for i in range(n - 1, 0, -1):
    for j in range(i - 1, -1, -1):
        if a[j] - a[i] > 0:
            diff = a[j] - a[i]
            a[i] += diff
            a[j] -= diff

print(' '.join([str(v) for v in a]))
