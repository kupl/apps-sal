n = int(input())
a = sorted([int(i) for i in input().split()])


s = 0
for i in range(0, n, 2):
    s += abs(a[i + 1] - a[i])

print(s)
