n = int(input())
a = [0 for i in range(n + 1)]
cnt = 0
for i in range(2, n + 1):
    if not a[i]:
        cnt += 1
        for j in range(i, n + 1, i):
            if not a[j]:
                a[j] = cnt
print(' '.join(str(i) for i in a[2:]))
