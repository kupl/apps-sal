n = int(input())
a = list(map(int, input().split()))

a.sort()
cap = []
res = []
for i in range(0, 2 * n - 1, 2):
    for j in range(i + 1, 2 * n, 2):
        f = 0
        first = 1
        cap = []
        for k in range(2 * n):
            if k == i or k == j:
                continue
            if first:
                f = a[k]
                first = 0
            else:
                first = 1
                cap.append(abs(a[k] - f))
        result = sum(cap)
        res.append(result)

print(min(res))
