x = int(input())

a = list(map(int, input().strip().split(' ')))
count = 0
sum = 0
for i in range(len(a)):
    sum += a[i]
z = int(sum / x)

for i in range(len(a)):
    if a[i] != z and a[i] > z:
        b = abs(z - a[i])
        a[i] = a[i] - b
        count += b
        a[i + 1] += b

    if a[i] != z and a[i] < z:
        b = abs(z - a[i])
        a[i] = a[i] + b
        count += b
        a[i + 1] -= b
print(count)
