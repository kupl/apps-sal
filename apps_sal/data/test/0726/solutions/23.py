(n, d) = input().split(' ')
n = int(n)
d = int(d)
x = input().split(' ')
for i in range(n):
    x[i] = int(x[i])
counter = 2
for i in range(n - 1):
    start = x[i]
    end = x[i + 1]
    if end - start < 2 * d:
        counter += 0
    elif end - start == 2 * d:
        counter += 1
    else:
        counter += 2
print(counter)
