(n, k, d) = list(map(int, input().split()))
a = sorted(list(map(int, input().split())))
b = [0] * n
i = j = 0
for i in range(n):
    while a[i] - a[j] > d:
        j += 1
    b[i] = j
c = [0] * n
for i in range(k - 1, n):
    c[i] = c[i - 1] + int(i - b[i] + 1 >= k and (b[i] == 0 or c[i - k] > c[b[i] - 2] or (b[i] == 1 and c[i - k] > c[0])))
print('YES' if n < 2 or c[n - 1] > c[n - 2] else 'NO')
