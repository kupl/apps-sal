(n, m) = list(map(int, input().split()))
a = list(map(int, input().split()))
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        if a[i] + a[j] <= m:
            a[i] += a[j]
            a[j] = 0
        else:
            break
a = [a[i] for i in range(n) if a[i] != 0]

print(len(a))
