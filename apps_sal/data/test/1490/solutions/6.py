(n, m) = list(map(int, input().split(' ')))
a = sorted(list(map(int, input().split(' '))))
b = []
j = 0
for i in range(1, 10 ** 9 + 1):
    if i > m:
        break
    if i <= m and (j >= n or i != a[j]):
        b.append(i)
        m -= i
    if j < n and i == a[j]:
        j += 1
print(len(b))
print(' '.join(map(str, b)))
