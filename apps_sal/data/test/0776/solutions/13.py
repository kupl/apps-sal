(a, b, c) = list(map(int, input().split()))
arr = [[], []]
for i in range(int(input())):
    (p, s) = input().split()
    pr = int(p)
    if s == 'USB':
        arr[0].append(pr)
    else:
        arr[1].append(pr)
arr[0].sort()
arr[1].sort()
pr = 0
n = 0
d = []
for j in range(min(a, len(arr[0]))):
    n += 1
    pr += arr[0][j]
d += arr[0][min(a, len(arr[0])):]
for j in range(min(b, len(arr[1]))):
    n += 1
    pr += arr[1][j]
    arr[1][j] = 10000000000.0
d += arr[1][min(b, len(arr[1])):]
d.sort()
for k in range(min(c, len(d))):
    n += 1
    pr += d[k]
print(n, pr)
