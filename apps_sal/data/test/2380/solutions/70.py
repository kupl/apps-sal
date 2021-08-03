n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
rep = sorted([tuple(map(int, input().split())) for i in range(m)], key=lambda x: -x[1])
i = 0
for b, c in rep:
    while i < n and b:
        if a[i] < c:
            a[i] = c
            i += 1
            b -= 1
        else:
            break
print(sum(a))
