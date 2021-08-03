def nod(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return (a + b)


n = int(input())
a = list(map(int, input().split()))
a.sort()
d = nod(a[1] - a[0], a[2] - a[1])
for i in range(2, n - 1):
    d = nod(a[i + 1] - a[i], d)
count = 0
for i in range(n - 1):
    count += ((a[i + 1] - a[i]) // d - 1)
print(count)
