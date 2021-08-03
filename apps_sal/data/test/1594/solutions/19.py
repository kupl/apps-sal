n, m = list(map(int, input().split()))
arr = []
for i in range(n):
    c, t = list(map(int, input().split()))
    arr.append(c * t)
i, p = 0, 0
v = [int(x) for x in input().split()]
for j in v:
    while (p < j):
        p, i = p + arr[i], i + 1
    print(i)
