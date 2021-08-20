n = int(input())
a = list(map(int, input().split()))
minimum = abs(a[0] - a[1])
counter = 0
a.sort()
for i in range(1, n - 1):
    if abs(a[i] - a[i + 1]) < minimum:
        minimum = abs(a[i] - a[i + 1])
for i in range(n - 1):
    if abs(a[i] - a[i + 1]) == minimum:
        counter += 1
print(minimum, counter, sep=' ')
