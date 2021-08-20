t = int(input())
a = list(map(int, input().split()))
b = []
max = a[t - 1]
i = t - 2
while i >= 0:
    if a[i] <= max:
        b.append(max - a[i] + 1)
    else:
        max = a[i]
        b.append(0)
    i = i - 1
b.insert(0, '0')
i = t - 1
while i >= 0:
    print(b[i], end=' ')
    i = i - 1
