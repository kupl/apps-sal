n = int(input())

a = input().split(' ')

for i in range(0, len(a)):
    a[i] = int(a[i])

print(abs(a[0] - a[1]), abs(a[0] - a[n - 1]))

for i in range(1, n - 1):
    print(min(abs(a[i] - a[i - 1]), abs(a[i] - a[i + 1])), max(abs(a[i] - a[0]), abs(a[i] - a[n - 1])))

print(abs(a[n - 1] - a[n - 2]), abs(a[n - 1] - a[0]))
