q = int(input())
res = []
for _ in range(q):
    n = int(input())
    a = list(map(int, input().split()))
    l = 0
    for m in range(1, n + 1):
        i = a.index(m)
        if i <= l:
            continue
        for j in range(i - 1, l - 1, -1):
            if a[j] < a[j + 1]:
                break
            a[j], a[j + 1] = a[j + 1], a[j]
        l = i

    res.append(' '.join(map(str, a)))

print(*res, sep='\n')
