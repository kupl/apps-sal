n = int(input())
a = [int(x) for x in input().split()]
print(a[1] - a[0], a[-1] - a[0])
for i in range(1, n - 1):
    print(min(a[i] - a[i - 1], a[i + 1] - a[i]), max(a[i] - a[0], a[-1] - a[i]))
print(a[-1] - a[-2], a[-1] - a[0])
