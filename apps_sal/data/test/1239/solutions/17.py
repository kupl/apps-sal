n = int(input())

a = list(map(int, input().split(' ')))

a = sorted(a)

m = a[1] - a[0]

for i in range(2, len(a)):
    if a[i] - a[i - 1] < m:
        m = a[i] - a[i - 1]

count = 0

for i in range(1, len(a)):
    if a[i] - a[i - 1] == m:
        count = count + 1

print(m, count)
