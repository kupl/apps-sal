(n, k) = tuple(map(int, input().strip().split(' ')))
l = 0
arr = []
cu = 0
yo = n % (2 * k + 1)
if yo >= k + 1 or yo == 0:
    for t in range(k + 1, n + 1, 2 * k + 1):
        arr.append(t)
else:
    for t in range(1, n + 1, 2 * k + 1):
        arr.append(t)
print(len(arr))
for k in arr:
    print(k, ' ', end='')
